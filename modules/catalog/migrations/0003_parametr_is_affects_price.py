# Generated by Django 2.2.12 on 2020-06-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200612_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametr',
            name='is_affects_price',
            field=models.BooleanField(default=False, verbose_name='Влияет на цену?'),
        ),
    ]