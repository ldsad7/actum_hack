# Generated by Django 2.2.3 on 2020-01-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurements', '0019_auto_20200125_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(verbose_name='Наименование товара'),
        ),
    ]
