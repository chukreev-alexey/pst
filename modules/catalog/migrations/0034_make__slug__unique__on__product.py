# Generated by Django 2.2.15 on 2020-08-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_gen__unique__slug__on__product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='ЧПУ'),
        ),
    ]