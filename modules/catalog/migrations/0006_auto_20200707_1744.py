# Generated by Django 2.2.14 on 2020-07-07 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_pricecombinations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='parametr',
        ),
        migrations.AddField(
            model_name='price',
            name='price_combination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price_by_parametres', to='catalog.PriceCombinations', verbose_name='Параметры'),
        ),
    ]