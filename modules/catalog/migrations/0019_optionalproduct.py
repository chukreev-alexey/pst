# Generated by Django 2.1.15 on 2020-08-10 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_category_filter_parametres'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionalProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Рекомендованные товары', max_length=255, verbose_name='Название')),
                ('sort', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
                ('show', models.BooleanField(default=False, verbose_name='Показывать?')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='optional_products', to=settings.ITCASE_CATALOG_PRODUCT_MODEL, verbose_name='Товар')),
                ('products', models.ManyToManyField(blank=True, to=settings.ITCASE_CATALOG_PRODUCT_MODEL, verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'Cвязанные товары',
                'verbose_name_plural': 'Cвязанные товары',
                'ordering': ['sort'],
            },
        ),
    ]
