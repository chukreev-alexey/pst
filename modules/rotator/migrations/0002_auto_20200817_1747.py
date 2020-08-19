# Generated by Django 2.1.15 on 2020-08-17 12:47

from django.conf import settings
from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rotator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotator',
            name='pages',
            field=mptt.fields.TreeManyToManyField(blank=True, related_name='rotator_rotator_set', to=settings.ITCASE_PAGES_PAGE_MODEL, verbose_name='Страницы'),
        ),
    ]