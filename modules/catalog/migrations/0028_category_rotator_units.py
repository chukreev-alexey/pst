# Generated by Django 2.1.15 on 2020-08-17 13:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.ITCASE_ROTATOR_ROTATOR_MODEL),
        ('catalog', '0027_auto_20200817_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rotator_units',
            field=models.ManyToManyField(blank=True, related_name='categories', to=settings.ITCASE_ROTATOR_ROTATOR_MODEL, verbose_name='Элементы ротатора'),
        ),
    ]
