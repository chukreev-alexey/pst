# Generated by Django 2.2.16 on 2020-10-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0044_set__template_categories_list__on__category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='filter_brand',
            field=models.BooleanField(default=True, verbose_name='Фильтровать по бренду'),
        ),
    ]
