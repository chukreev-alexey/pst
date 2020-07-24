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


class PriceCombinations(models.Model):
    data = models.ManyToManyField(
        ProductParametr,
        related_name='combination_parametres',
        blank=True,
        verbose_name='Параметры')

    class Meta(object):
        verbose_name = 'Параметры комплектации'
        verbose_name_plural = 'Варианты комплектаций'

    def __str__(self):
        data = [f'{i.parametr.name}: {i.value}' for i in self.data.all()]
        return '; '.join(data)


class Price(models.Model):
    product = models.ForeignKey(Product, related_name='prices',
                                verbose_name=Product._meta.verbose_name,
                                on_delete=models.CASCADE)
    product_article = models.CharField('Артикул', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField('Количество в наличии')

    price_combination = models.ForeignKey(
        PriceCombinations,
        related_name='price_by_parametres',
        blank=True, null=True,
        verbose_name='Параметры', on_delete=models.CASCADE)

    class Meta(object):
        verbose_name = 'Цена комплектации'
        verbose_name_plural = 'Цены комплектаций'

    def __str__(self):
        if self.price_combination:
            return f'{self.price_combination.data.first()}: {self.price}'
        else:
            return 'None'
