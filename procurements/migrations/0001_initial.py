# Generated by Django 2.2.3 on 2020-01-25 20:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('inn', models.CharField(max_length=64, null=True, verbose_name='ИНН заказчика')),
                ('kpp', models.CharField(max_length=64, null=True, verbose_name='КПП заказчика')),
                ('num_of_contracts', models.IntegerField(null=True, verbose_name='Количество контрактов на ПП')),
                ('sum_of_contracts', models.FloatField(null=True, verbose_name='Сумма контрактов на ПП')),
                ('legal_form', models.CharField(choices=[('legal entity', 'юридическое лицо'), ('individual', 'физическое лицо')], default='legal entity', max_length=32, verbose_name='Организационно-правовая форма')),
                ('email', models.CharField(max_length=64, null=True, verbose_name='E-Mail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование характеристики')),
                ('value', models.FloatField(null=True, verbose_name='Значение характеристики')),
                ('measurement', models.CharField(max_length=64, verbose_name='Измерение характеристики')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование цвета')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fio', models.CharField(max_length=255, null=True, verbose_name='ФИО контактного лица')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='E-Mail контактного лица')),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='Телефон контактного лица')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('registry_number', models.CharField(max_length=255, verbose_name='Реестровый номер контракта')),
                ('number', models.CharField(max_length=255, verbose_name='Номер контракта')),
                ('status', models.CharField(choices=[('concluded', 'Заключен'), ('terminated', 'Расторгнут'), ('refusal', 'Отказ от заключения'), ('executed', 'Исполнен'), ('data entry', 'Ввод сведений')], default='concluded', max_length=32, verbose_name='Статус контракта')),
                ('price', models.FloatField(null=True, verbose_name='Цена контракта')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContractorItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Адрес поставщика закупки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование страны')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Адрес заказчика закупки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Название закона')),
                ('text', models.TextField(null=True, verbose_name='Текст закона')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование материала')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('number', models.CharField(max_length=255, unique=True, verbose_name='Номер оферты')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Дата начала действия оферты')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Дата окончания действия оферты')),
                ('price', models.FloatField(null=True, verbose_name='Стимость оферты')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OKPD2ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование вида товаров (ОКПД2)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование производителя')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.IntegerField(null=True, verbose_name='ID товара')),
                ('name', models.TextField(verbose_name='Наименование товара')),
                ('warranty_period', models.IntegerField(null=True, verbose_name='Гарантийный срок товара (в днях)')),
                ('num_of_offers', models.IntegerField(null=True, verbose_name='Количество действующих оферт')),
                ('sum_of_offers', models.FloatField(null=True, verbose_name='Сумма в составе контрактов')),
                ('num_of_contracts', models.IntegerField(null=True, verbose_name='Количество контрактов')),
                ('characteristics', models.ManyToManyField(blank=True, to='procurements.Characteristic', verbose_name='Характеристики')),
                ('colour', models.ManyToManyField(blank=True, to='procurements.Colour', verbose_name='Цвет товара')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.Country', verbose_name='Страна происхождения товара')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.Material', verbose_name='Материал товара')),
                ('okpd2_product_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.OKPD2ProductType', verbose_name='Вид товаров (ОКПД2)')),
                ('producer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.Producer', verbose_name='Производитель товара')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование вида продукции')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('quantity', models.BigIntegerField(verbose_name='Количество товаров данного вида')),
                ('price', models.FloatField(verbose_name='Цена одной единицы товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procurements.Product', verbose_name='Товар закупки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование вида товаров')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Способ закупки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Вид закупки')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование региона')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='procurements.BaseUser')),
                ('external_id', models.IntegerField(null=True, verbose_name='ID поставщика')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Наименование поставщика')),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='Телефон организации')),
                ('digital_signature', models.CharField(choices=[('Yes', 'Есть'), ('No', 'Нет')], default='No', max_length=32, verbose_name='Наличие ЭП\\Отсутствие ЭП')),
                ('offer', models.CharField(choices=[('Yes', 'Есть'), ('No', 'Нет')], default='No', max_length=32, verbose_name='Загружал\\не загружал оферты')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'abstract': False,
            },
            bases=('procurements.baseuser',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='procurements.BaseUser')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное наименование заказчика')),
                ('short_name', models.CharField(max_length=255, verbose_name='Краткое наименование заказчика')),
                ('contact_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.ContactPerson', verbose_name='Контактное лицо')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
                'abstract': False,
            },
            bases=('procurements.baseuser',),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Название закупки')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Дата начала торгов')),
                ('end_date', models.DateTimeField(null=True, verbose_name='Дата конца торгов')),
                ('registry_number', models.CharField(max_length=64, null=True, verbose_name='Реестровый номер')),
                ('number', models.CharField(max_length=255, null=True, verbose_name='Номер (?) закупки')),
                ('title', models.TextField(null=True, verbose_name='Предмет закупки')),
                ('external_id', models.IntegerField(null=True, verbose_name='ID закупки')),
                ('price', models.BigIntegerField(null=True, verbose_name='Стоимость закупки')),
                ('status', models.CharField(choices=[('took place', 'Проведена'), ("didn't take place", 'Не состоялась'), ('deregistered', 'Снята с публикации'), ('completed', 'Прием предложений завершен'), ('canceled', 'Отменена'), ('data entry', 'Ввод сведений')], default='took place', max_length=32, verbose_name='Статус закупки')),
                ('url', models.URLField(null=True, verbose_name='Ссылка на закупку')),
                ('contractor_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.ContractorItem', verbose_name='Поставщик закупки + адрес')),
                ('law', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.Law', verbose_name='Закон-основание')),
                ('method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.PurchaseMethod', verbose_name='Способ закупки')),
                ('offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.Offer', verbose_name='Оферта по итогам')),
                ('participant_items', models.ManyToManyField(blank=True, to='procurements.CustomerItem', verbose_name='Заказчики закупки + их адреса')),
                ('product_items', models.ManyToManyField(blank=True, to='procurements.ProductItem', verbose_name='Товары в закупке')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.PurchaseType', verbose_name='Вид закупки')),
            ],
            options={
                'verbose_name': 'Закупка',
                'verbose_name_plural': 'Закупки',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.ProductType', verbose_name='Вид товаров'),
        ),
        migrations.AddField(
            model_name='product',
            name='production_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.ProductionType', verbose_name='Вид продукции'),
        ),
        migrations.AddField(
            model_name='contractoritem',
            name='regions',
            field=models.ManyToManyField(blank=True, to='procurements.Region', verbose_name='Регионы поставки'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='production_types',
            field=models.ManyToManyField(blank=True, to='procurements.ProductionType', verbose_name='ТОП 3 продукции'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='registration_region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='procurements.Region', verbose_name='Регион регистрации'),
        ),
        migrations.AddField(
            model_name='customeritem',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procurements.Customer', verbose_name='Заказчик закупки'),
        ),
        migrations.AddField(
            model_name='contractoritem',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procurements.Contractor', verbose_name='Поставщик закупки'),
        ),
    ]
