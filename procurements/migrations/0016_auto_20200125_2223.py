# Generated by Django 2.2.3 on 2020-01-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurements', '0015_auto_20200125_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='registry_number',
            field=models.CharField(max_length=64, null=True, verbose_name='Реестровый номер'),
        ),
    ]