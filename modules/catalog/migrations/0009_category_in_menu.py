# Generated by Django 2.2.14 on 2020-07-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_category_on_main_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='in_menu',
            field=models.BooleanField(default=False, verbose_name='Отображать в меню?'),
        ),
    ]