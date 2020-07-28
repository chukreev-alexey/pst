# Generated by Django 2.2.14 on 2020-07-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_category_in_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='border',
            field=models.BooleanField(default=False, verbose_name='Выделить товар'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_action',
            field=models.BooleanField(default=False, verbose_name='Учавствует в акции?'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_hit',
            field=models.BooleanField(default=False, verbose_name='Хит?'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_recommended',
            field=models.BooleanField(default=False, verbose_name='Рекомендованный товар?'),
        ),
    ]
