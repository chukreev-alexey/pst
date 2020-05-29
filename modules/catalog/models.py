from django.db import models
from django.urls import reverse_lazy

from tinymce_4.fields import TinyMCEModelField
from filebrowser.fields import FileBrowseField
from mptt.models import MPTTModel

from itcase_catalog.models import ProductBase, CategoryBase
from itcase_catalog.models import OptionFieldBase
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

    def get_price_by_color(self, color_id):
        if self.color_prices.filter(id=color_id).exists():
            return self.color_prices.get(id=color_id).price
        else:
            return self.price

    def get_price_color_dict(self):
        if self.color_prices:
            return {cp.color.name: cp.price for cp in self.color_prices.all()}
        return None


class ProductColors(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    sort = models.PositiveSmallIntegerField('Порядок', default=0)

    class Meta(object):
        ordering = ['sort']
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета товаров'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = FileBrowseField('Изображение', format='image', max_length=255,
                            blank=True)
    sort = models.PositiveSmallIntegerField('Позиция', default=0)
    color = models.ForeignKey(ProductColors, related_name='color_images',
                              verbose_name='Цвет',
                              on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='images',
                                verbose_name=Product._meta.verbose_name,
                                on_delete=models.CASCADE)

    class Meta(object):
        ordering = ['sort']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.image.original_filename


class PickingPrice(models.Model):
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    color = models.ForeignKey(ProductColors, related_name='product_prices',
                              verbose_name='Цвет',
                              on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, related_name='color_prices',
                                verbose_name=Product._meta.verbose_name,
                                on_delete=models.CASCADE)

    class Meta(object):
        verbose_name = 'Цена комплектации'
        verbose_name_plural = 'Цены Комплектаций'

    def __str__(self):
        return f'{self.color.name}: {self.price}'
