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
from mptt.models import MPTTModel

from tinymce_4.fields import TinyMCEModelField
from filebrowser.fields import FileBrowseField

from itcase_catalog.models import ProductBase, CategoryBase
from itcase_common.models import SEOModel


class Category(MPTTModel, CategoryBase, SEOModel):
    from mptt.fields import TreeForeignKey
    from django.core.validators import validate_slug

    slug = models.SlugField('Slug', unique=True, validators=[validate_slug])
    parent = TreeForeignKey('self', related_name='children',
                            verbose_name='Родительский элемент',
                            on_delete=models.SET_NULL, blank=True, null=True)

    content = TinyMCEModelField('Подробное описание', blank=True)
    image = FileBrowseField('Изображение', format='image', max_length=255,
                            blank=True)

    class Meta(CategoryBase.Meta):
        pass

    def get_products(self):
        """Return products from all nested categories."""
        descendants = self.get_descendants(include_self=True)

        return Product.objects.filter(category__in=descendants)

    def get_absolute_url(self):
        if self.level == 2:
            url = reverse_lazy('category-detail', args=[str(self.parent.slug)])
            return str(url) + '?filter-category=%s' % self.pk

        return reverse_lazy('category-detail', args=[str(self.slug)])


class Brand(models.Model):

    name = models.CharField('Название', max_length=255)
    sort = models.PositiveSmallIntegerField('Порядок сортировки', default=0)

    class Meta(object):
        ordering = ['sort', ]
        verbose_name = 'Бренд'
        verbose_name_plural = verbose_name + 'ы'

    def __str__(self):
        return self.name


class Parametr(models.Model):
    name = models.CharField('Название', max_length=255)
    query_name = models.SlugField('Query name')
    is_affects_price = models.BooleanField('Влияет на цену?',
                                           default=False)
    filter_by = models.BooleanField('Фильтровать по параметру?',
                                    default=False)

    class Meta(object):
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры товаров'

    def __str__(self):
        return self.name


class ProductParametr(models.Model):
    parametr = models.ForeignKey(Parametr, related_name='product_parametres',
                                 verbose_name='Параметры продуктов',
                                 on_delete=models.CASCADE)
    value = models.CharField('Значение параметра', max_length=255)

    class Meta(object):
        unique_together = ('parametr', 'value')
        verbose_name = 'Вариант параметра'
        verbose_name_plural = 'Варианты параметра товара'

    def __str__(self):
        return f'{self.parametr.name}: {self.value}'


class Product(ProductBase):
    brand = models.ForeignKey(Brand,
                              related_name='products', verbose_name='Бренд',
                              on_delete=models.SET_NULL, blank=True, null=True)
    description = TinyMCEModelField('Подробное описание', blank=True)
    related_products = models.ManyToManyField(
        'self', blank=True, verbose_name='Комплектующие')
    pdf_instructtion = FileBrowseField('Инструкция', format='file',
                                       max_length=255, blank=True)
    pdf_components = FileBrowseField('Комплектующие', format='file',
                                     max_length=255, blank=True)
    scheme = FileBrowseField('Схема', format='image',
                             max_length=255, blank=True)

    parametres = models.ManyToManyField(
        ProductParametr,
        related_name='products',
        blank=True,
        verbose_name='Параметры')

    class Meta(ProductBase.Meta):
        pass

    def get_first_image(self):
        """Return first image."""
        if self.image and self.image.exists:
            return self.image

        for image in self.get_images():
            return image

    def get_images(self):
        """Yield over not None and exist images."""
        for image in self.images.all():
            if not image.image or not image.image.exists:
                continue
            yield image

    def get_parametres_dict(self):
        parametres = set(p.parametr for p in self.parametres.all())
        return {p: self.parametres.filter(parametr=p) for p in parametres}
