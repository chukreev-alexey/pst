# Generated by Django 2.1.15 on 2020-08-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0036_add__sort__to__product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
    ]