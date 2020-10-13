# -*- coding: utf-8 -*-
#
# Copyright 2020 ItCase (info@itcase.pro)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models

from django.urls import reverse_lazy
from django.core.validators import validate_slug

from filebrowser.fields import FileBrowseField
from mptt.fields import TreeForeignKey, TreeManyToManyField
from mptt.models import MPTTModel
from tinymce_4.fields import TinyMCEModelField

from itcase_catalog.models import ProductBase, CategoryBase
from itcase_common.models import SEOModel, ChangeCreateModel
from itcase_common.models.mixins import FieldExistsMixin

from ..conf import get_settings


class Measurement(models.Model):

    name = models.CharField('Обозначение', max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField('Название', max_length=255)
    sort = models.PositiveSmallIntegerField('Порядок сортировки', default=0)

    class Meta:
        ordering = ('sort', 'name')
        verbose_name = 'Бренд'
        verbose_name_plural = verbose_name + 'ы'

    def __str__(self):
        return self.name


class Parametr(models.Model):

    name = models.CharField('Название', max_length=255)
    query_name = models.SlugField('Query name')
    is_affects_price = models.BooleanField('Влияет на цену?', default=False)
    filter_by = models.BooleanField('Фильтровать по параметру?', default=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры товаров'

    def __str__(self):
        return self.name


class ProductParametr(models.Model):

    parametr = models.ForeignKey(Parametr,
                                 related_name='product_parametres',
                                 verbose_name='Параметры продуктов',
                                 on_delete=models.CASCADE)
    value = models.CharField('Значение параметра', max_length=255)

    class Meta:
        ordering = ('parametr', 'value')
        unique_together = ('parametr', 'value')
        verbose_name = 'Вариант параметра'
        verbose_name_plural = 'Варианты параметра товара'

    def __str__(self):
        return f'{self.parametr.name}: {self.value}'


class Category(MPTTModel, CategoryBase, SEOModel, ChangeCreateModel):

    slug = models.SlugField('Slug',
                            max_length=255,
                            unique=True,
                            validators=[validate_slug])
    parent = TreeForeignKey('self',
                            related_name='children',
                            verbose_name='Родительский элемент',
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True)

    content = TinyMCEModelField('Подробное описание', blank=True)
    image = FileBrowseField('Изображение',
                            format='image',
                            max_length=255,
                            blank=True)

    on_main_page = models.BooleanField('Отображать на главной странице?',
                                       default=False)
    in_menu = models.BooleanField('Отображать в меню?', default=False)

    filter_parametres = models.ManyToManyField(
        Parametr,
        related_name='categories',
        verbose_name='Параметры для фильтра',
        blank=True)

    template_categories_list = models.BooleanField(
        'Шаблон только с категориями', default=False)
    template_groups_type_selector = models.BooleanField(
        'Шаблон с категориями и товарами', default=False)

    rotator_units = models.ManyToManyField(
        get_settings('ITCASE_ROTATOR_ROTATOR_MODEL'),
        related_name='categories',
        verbose_name='Элементы ротатора',
        blank=True)

    active = models.BooleanField('Показывать', default=True)

    filter_brand = models.BooleanField('Фильтровать по бренду', default=True)

    class Meta(CategoryBase.Meta):
        pass

    def get_absolute_url(self):
        if self.level == 2:
            return reverse_lazy('subcategory-detail',
                                args=[self.parent.slug, self.slug])
        return reverse_lazy('category-detail', args=[self.slug])

    def get_children_active(self):
        return self.children.filter(active=True)

    def get_products(self):
        """Return products from all nested categories."""
        descendants = self.get_descendants(include_self=True)

        return Product.objects.filter(categories__in=descendants)

        return reverse_lazy('category-detail', args=[str(self.slug)])


class CategorySectionAtribute(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='sections',
                                 verbose_name=Category._meta.verbose_name,
                                 on_delete=models.CASCADE)
    name = models.CharField('Название', blank=True, max_length=255)
    content = TinyMCEModelField('Контeнт', blank=True)
    sort = models.PositiveSmallIntegerField('Позиция', default=0)
    show = models.BooleanField('Показывать?', default=True)

    class Meta(object):
        ordering = ['sort']
        verbose_name = 'Вкладка'
        verbose_name_plural = 'Вкладки'

    def __str__(self):
        return self.name


class Product(ProductBase, FieldExistsMixin, SEOModel, ChangeCreateModel):

    brand = models.ForeignKey(Brand,
                              related_name='products',
                              verbose_name='Бренд',
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)

    price = models.DecimalField('Цена',
                                max_digits=10,
                                decimal_places=2,
                                blank=True,
                                null=True)
    article = models.CharField(verbose_name='Артикул',
                               max_length=255,
                               blank=True,
                               null=True)

    recommend_categories = models.ManyToManyField(
        Category, blank=True, verbose_name='Рекомендуем категории')

    in_hit = models.BooleanField('Хит?', default=False)
    in_action = models.BooleanField('Учавствует в акции?', default=False)
    in_recommended = models.BooleanField('Рекомендованный товар?',
                                         default=False)

    border = models.BooleanField('Выделить товар', default=False)

    parametres = models.ManyToManyField(ProductParametr,
                                        related_name='products',
                                        blank=True,
                                        verbose_name='Параметры')

    measuring = models.ForeignKey(Measurement,
                                  related_name='products',
                                  verbose_name='Единица измерения',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    categories = TreeManyToManyField(
        Category,
        related_name='products',
        verbose_name=Category._meta.verbose_name_plural)

    slug = models.SlugField('ЧПУ', max_length=255, unique=True)

    content = TinyMCEModelField('Описание', blank=True)
    sort = models.PositiveSmallIntegerField('Порядок', default=0)
    short_description = models.TextField('Краткое описание',
                                         blank=True,
                                         null=True)

    active = models.BooleanField(
        'Показывать',
        default=True,
        help_text='Если отключёно, элемент не будет отображаться на сайте')

    class Meta(ProductBase.Meta):
        ordering = ('sort', 'name', 'price')

    def get_absolute_url(self):
        return reverse_lazy('product-detail', args=[self.slug])

    def get_all_images(self):
        images = []
        for image in self.get_images():
            images.append((image.image, image.image_description))
        for price in self.get_prices_images():
            images.append((price.image, price.image_description))
        return images

    def get_first_image(self):
        """Return first image."""
        if self.image and self.image.exists:
            return self.image.image

        for image in self.get_images():
            return image
        # if object product does not have images then get image from prices
        # use "_" because here is not need image description
        for image in self.get_prices_images():
            return image

    def get_images(self):
        """Yield over not None and exist images."""
        for image in self.images.all():
            if not image.image or not image.image.exists:
                continue
            yield image

    def get_optional_products(self):
        return self.optional_products.filter(show=True)

    def get_prices_images(self):
        for price in self.prices.exclude(image__exact='').exclude(show=False):
            if not price.image.exists:
                continue
            price.image.price_pk = price.pk
            yield price

    def has_sections(self):
        return self.sections.exists()


class SectionAtribute(models.Model):
    product = models.ForeignKey(Product,
                                related_name='sections',
                                verbose_name=Product._meta.verbose_name,
                                on_delete=models.CASCADE)
    section_name = models.CharField('Название', blank=True, max_length=255)
    section_content = TinyMCEModelField('Контeнт', blank=True)
    sort = models.PositiveSmallIntegerField('Позиция', default=0)
    show = models.BooleanField('Показывать?', default=True)

    class Meta(object):
        ordering = ['sort']
        verbose_name = 'Вкладка параметров'
        verbose_name_plural = 'Вкладки параметров'


class OptionalProduct(models.Model):
    product = models.ForeignKey(Product,
                                related_name='optional_products',
                                verbose_name=Product._meta.verbose_name,
                                on_delete=models.CASCADE)
    name = models.CharField('Название',
                            blank=True,
                            max_length=255,
                            default='Рекомендованные товары')
    products = models.ManyToManyField(Product,
                                      blank=True,
                                      verbose_name='Товары')
    sort = models.PositiveSmallIntegerField('Позиция', default=0)
    show = models.BooleanField('Показывать?', default=False)

    class Meta(object):
        ordering = ['sort']
        verbose_name = 'Cвязанные товары'
        verbose_name_plural = 'Cвязанные товары'
