# Generated by Django 2.2.3 on 2020-01-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='production_types',
            field=models.ManyToManyField(blank=True, to='procurements.ProductionType', verbose_name='ТОП 3 продукции'),
        ),
    ]
