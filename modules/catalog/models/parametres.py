from django.db import models

from filebrowser.fields import FileBrowseField
from smart_selects.db_fields import ChainedForeignKey

from .catalog import Product, Parametr, ProductParametr


class ProductImage(models.Model):
    image = FileBrowseField('Изображение', format='image', max_length=255,
                            blank=True)
    sort = models.PositiveSmallIntegerField('Позиция', default=0)
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
    old_price = models.DecimalField('Старая цена',
                                    max_digits=10,
                                    decimal_places=2,
                                    blank=True,
                                    null=True)
    amount = models.PositiveIntegerField('Количество в наличии',
                                         blank=True, null=True)

    price_combination = models.ForeignKey(
        PriceCombinations,
        related_name='price_by_parametres',
        blank=True, null=True,
        verbose_name='Параметры', on_delete=models.CASCADE)

    image = FileBrowseField('Изображение', format='image', max_length=255,
                            blank=True)
    image_description = models.CharField('Описание изображения',
                                         max_length=255,
                                         blank=True, null=True)

    class Meta(object):
        verbose_name = 'Цена комплектации'
        verbose_name_plural = 'Цены комплектаций'

    def __str__(self):
        if self.price_parametres:
            return f'{self.price}'
        else:
            return 'None'


# TODO: maybe add amount for each parametr_value
class SeparateParametrPicking(models.Model):
    price = models.ForeignKey(Price, related_name='price_parametres',
                              verbose_name=Price._meta.verbose_name,
                              on_delete=models.CASCADE)

    parametr = models.ForeignKey(Parametr,
                                 related_name='separated_product_parametres',
                                 verbose_name='Параметр',
                                 on_delete=models.DO_NOTHING)
    parametr_value = ChainedForeignKey(
        ProductParametr,
        related_name='separated_product_parametres',
        chained_field="parametr",
        chained_model_field="parametr",
        show_all=False,
        auto_choose=True,
        sort=True)
    sort = models.PositiveSmallIntegerField('Позиция', default=0)

    class Meta(object):
        ordering = ['sort']
        verbose_name = 'Параметр комплектаций'
        verbose_name_plural = 'Параметры комплектаций'
