# Generated by Django 2.2.14 on 2020-07-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20200729_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='measuring',
            field=models.PositiveSmallIntegerField(choices=[(0, 'м.п.'), (1, 'м.кв.'), (2, 'шт.')], default=0, verbose_name='Единицы измерения'),
            preserve_default=False,
        ),
    ]
