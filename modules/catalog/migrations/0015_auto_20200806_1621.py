# Generated by Django 2.1.15 on 2020-08-06 11:21

from django.db import migrations, models
import django.db.models.deletion


def remove_old_produc_measuring(apps, schema_editor):
    Product = apps.get_model('catalog', 'Product')
    for product in Product.objects.all():
        product.measuring = None
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_price_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='measuring',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, 'м.п.'), (1, 'м.кв.'), (2, 'шт.')], default=0, verbose_name='Единицы измерения'),
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Обозначение')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': 'Единицы измерения',
            },
        ),
        migrations.RunPython(remove_old_produc_measuring),
        migrations.AlterField(
            model_name='product',
            name='measuring',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.Measurement', verbose_name='Единица измерения'),
        ),
    ]