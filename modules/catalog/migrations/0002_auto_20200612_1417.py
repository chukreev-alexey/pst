# Generated by Django 2.2.12 on 2020-06-12 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Параметры товаров',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_article', models.CharField(max_length=255, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество в наличии')),
            ],
            options={
                'verbose_name': 'Цена комплектации',
                'verbose_name_plural': 'Цены Комплектаций',
            },
        ),
        migrations.CreateModel(
            name='ProductParametr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значение параметра')),
                ('filter_by', models.BooleanField(default=False, verbose_name='Фильтровать по параметру?')),
                ('parametr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parametres', to='catalog.Parametr', verbose_name='Параметры продуктов')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parametres', to=settings.ITCASE_CATALOG_PRODUCT_MODEL, verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Параметры товаров',
            },
        ),
        migrations.AlterField(
            model_name='productimage',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='color_images', to='catalog.ProductParametr', verbose_name='Цвет'),
        ),
        migrations.DeleteModel(
            name='PickingPrice',
        ),
        migrations.DeleteModel(
            name='ProductColors',
        ),
        migrations.AddField(
            model_name='price',
            name='parametr',
            field=models.ManyToManyField(blank=True, related_name='price_by_parametres', to='catalog.ProductParametr', verbose_name='Параметры'),
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to=settings.ITCASE_CATALOG_PRODUCT_MODEL, verbose_name='Товар'),
        ),
    ]