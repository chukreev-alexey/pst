from django.db import models

from filebrowser.fields import FileBrowseField

from .catalog import Product, ProductParametr


class ProductImage(models.Model):
    image = FileBrowseField('Изображение', format='image', max_length=255,
                            blank=True)
    sort = models.PositiveSmallIntegerField('Позиция', default=0)
    color = models.ForeignKey(ProductParametr, related_name='color_images',
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


class Price(models.Model):
    product = models.ForeignKey(Product, related_name='prices',
                                verbose_name=Product._meta.verbose_name,
                                on_delete=models.CASCADE)
    product_article = models.CharField('Артикул', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField('Количество в наличии')

    parametr = models.ManyToManyField(
        ProductParametr,
        related_name='price_by_parametres',
        blank=True,
        verbose_name='Параметры')

    class Meta(object):
        verbose_name = 'Цена комплектации'
        verbose_name_plural = 'Цены Комплектаций'

    def __str__(self):
        return f'{self.parametr.first()}: {self.price}'
