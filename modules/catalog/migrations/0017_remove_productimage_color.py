# Generated by Django 2.1.15 on 2020-08-10 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20200807_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='color',
        ),
    ]
