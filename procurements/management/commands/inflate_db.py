import csv
import re

from django.core.management import BaseCommand

# import os
from procurements.models import Customer, Region, ContactPerson, ProductionType, Contractor, Product, Producer, Country, \
    ProductType, Characteristic, Material, Purchase, PurchaseMethod, CustomerItem, ProductItem, ContractorItem


class Command(BaseCommand):
    help = 'Наполняет базу Procurements данными из csv'

    def customer_update(self, num=500):
        with open(r'C:\Users\Eduard\Desktop\Projects\true_actum_hack\data\х Заказчики.csv', 'r',
                  encoding='cp1251') as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader):
                if i > num:
                    break
                for key, value in row.items():
                    if value == "NULL":
                        row[key] = None
                region = None
                if row['Регион регистрации'] is not None:
                    region, _ = Region.objects.update_or_create(
                        name=row['Регион регистрации']
                    )
                contact_person = None
                if row['ФИО контактного лица'] is not None:
                    contact_person, _ = ContactPerson.objects.update_or_create(
                        fio=row['ФИО контактного лица'],
                        email=row['E-Mail контактного лица'],
                        phone=row['Телефон контактного лица']
                    )
                sum_of_contracts = None
                if row['Сумма контрактов на ПП'] is not None:
                    sum_of_contracts = float(row['Сумма контрактов на ПП'])
                num_of_contracts = None
                if row['Количество контрактов на ПП'] is not None:
                    num_of_contracts = int(row['Количество контрактов на ПП'])
                customer, _ = Customer.objects.update_or_create(
                    full_name=row['Полное наименование заказчика'],
                    short_name=row['Краткое наименование заказчика'],
                    defaults={
                        'inn': row['ИНН заказчика'],
                        'kpp': row['КПП заказчика'],
                        'legal_form': row['Организационно правовая форма'],
                        'num_of_contracts': num_of_contracts or 0,
                        'sum_of_contracts': sum_of_contracts or 0,
                        'registration_region': region,
                        'contact_person': contact_person,
                        'email': row['E-Mail']
                    }
                )

                if row['ТОП 3 продукции'] is not None:
                    types = [elem.strip() for elem in row['ТОП 3 продукции'].split(';') if elem.strip()]
                    types = [ProductionType.objects.update_or_create(name=elem)[0] for elem in types]
                    customer.production_types.add(*types)
                customer.save()

    def contractor_update(self, num=500):
        with open(
                r'C:\Users\Eduard\Desktop\Projects\true_actum_hack\data\х Поставщики.csv', 'r', encoding='cp1251'
        ) as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader):
                if i > num:
                    break
                for key, value in row.items():
                    if value == "NULL":
                        row[key] = None
                region = None
                if row['Регион регистрации'] is not None:
                    region, _ = Region.objects.update_or_create(
                        name=row['Регион регистрации']
                    )
                sum_of_contracts = None
                if row['Сумма контрактов на ПП'] is not None:
                    sum_of_contracts = float(row['Сумма контрактов на ПП'])
                num_of_contracts = None
                if row['Количество контрактов на ПП'] is not None:
                    num_of_contracts = int(row['Количество контрактов на ПП'])
                contractor, _ = Contractor.objects.update_or_create(
                    name=row['Нименование поставщика'],
                    external_id=row['ID'],
                    defaults={
                        'inn': row['ИНН поставщика'],
                        'kpp': row['КПП поставщика'],
                        'registration_region': region,
                        'num_of_contracts': num_of_contracts or 0,
                        'sum_of_contracts': sum_of_contracts or 0,
                        'legal_form': row['Тип поставщика'],
                        'email': row['E-Mail'],
                        'phone': row['Телефон организации'],
                        'digital_signature': Contractor.REVERSED_STATUS[row['Наличие ЭП\Отсутствие ЭП']],
                        'offer': Contractor.REVERSED_STATUS[row['Загружал\не загружал оферты']]
                    }
                )
                if row['ТОП 3 продукции'] is not None:
                    types = [elem.strip() for elem in row['ТОП 3 продукции'].split(';') if elem.strip()]
                    types = [ProductionType.objects.update_or_create(name=elem)[0] for elem in types]
                    contractor.production_types.add(*types)

    @staticmethod
    def return_value_or_none(cls, row, name):
        elem = None
        if row[name] is not None:
            elem, _ = cls.objects.get_or_create(
                name=row[name]
            )
        return elem

    def product_update(self, num=500):
        with open(
                r'C:\Users\Eduard\Desktop\Projects\true_actum_hack\data\х СТЕ все.csv', 'r', encoding='cp1251'
        ) as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader):
                if i > num:
                    break
                for key, value in row.items():
                    if value == "NULL":
                        row[key] = None
                producer = self.return_value_or_none(Producer, row, 'Производитель')
                country = self.return_value_or_none(Country, row, 'Страна происхождения')
                production_type = self.return_value_or_none(ProductionType, row, 'Вид продукции')
                product_type = self.return_value_or_none(ProductType, row, 'Вид товаров')
                material = self.return_value_or_none(Material, row, 'Материал')
                warranty_period = None
                if row['Гарантийный срок'] is not None:
                    warranty_period = int(row['Гарантийный срок'])
                product, _ = Product.objects.update_or_create(
                    name=row['Наменование'],
                    producer=producer,
                    defaults={
                        'country': country,
                        'production_type': production_type,
                        'product_type': product_type,
                        'material': material,
                        'warranty_period': warranty_period,
                        'num_of_offers': row['Количество действующих оферт'] or 0,
                        'sum_of_offers': row['Сумма в составе контрактов'] or 0,
                        'num_of_contracts': row['Количество контрактов'] or 0
                    }
                )
                for characteristic in ['Длина', 'Ширина', 'Высота', 'Диаметр', 'Вес', 'Объем']:
                    if row[characteristic] is not None:
                        value, measurement = row[characteristic].split()
                        characteristic, _ = Characteristic.objects.update_or_create(
                            name=characteristic,
                            value=float(value),
                            measurement=measurement
                        )
                        product.characteristics.add(characteristic)

                if row['Цвет'] is not None:
                    product.colour.add(*[colour.strip() for colour in row['Цвет'].split() if colour.strip()])
                product.save()

    def procurement_update(self, num=500):
        with open(
                r'C:\Users\Eduard\Desktop\Projects\true_actum_hack\data\х Контракты 2 1 часть.csv', 'r', encoding='cp1251'
        ) as f:
            reader = csv.DictReader(f, delimiter=';')
            for i, row in enumerate(reader):
                if i > num:
                    break
                for key, value in row.items():
                    if value == "NULL":
                        row[key] = None
                purchase_method = self.return_value_or_none(PurchaseMethod, row, 'Способ закупки')
                end_date = row['Дата заключения']
                if end_date[4] != '-':
                    date_, time_ = end_date.split()
                    date_ = date_.split('.')
                    if len(time_) == 4:
                        time_ = '0' + time_
                    end_date = date_[-1] + '-' + date_[-2] + '-' + date_[-3] + ' ' + time_
                purchase, _ = Purchase.objects.update_or_create(
                    method=purchase_method,
                    end_date=end_date,
                    registry_number=row['Реестровый номер'],
                    number=row['Номер'],
                    title=row['Предмет'],

                )
                region = self.return_value_or_none(Region, row, 'Регион заказчика')
                customer, _ = Customer.objects.get_or_create(
                    full_name=row['Заказчик'],
                    defaults={
                        'registration_region': region,
                        'inn': row['ИНН заказчика'],
                        'kpp': row['КПП заказчика'],
                    }
                )
                customer_item, _ = CustomerItem.objects.update_or_create(
                    customer=customer,
                    address=row['Регион заказчика']
                )
                purchase.participant_items.add(customer_item)

                product = self.return_value_or_none(Product, row, 'Наименование позиции')
                if product is not None:
                    product_item, _ = ProductItem.objects.update_or_create(
                        product=product,
                        quantity=int(float(row['Количество'])),
                        price=float(row['Цена за единицу'])
                    )
                    purchase.product_items.add(product_item)

                region = self.return_value_or_none(Region, row, 'Регион заказчика')
                contractor, _ = Contractor.objects.update_or_create(
                    name=row['Поставщик'],
                    defaults={
                        'registration_region': region,
                        'inn': row['ИНН поставщика'],
                        'kpp': row['КПП поставщика']
                    }
                )
                contractor_item, _ = ContractorItem.objects.update_or_create(
                    contractor=contractor,
                    address=row['Регион поставщика']
                )
                purchase.contractor_item = contractor_item
                purchase.save()

    def handle(self, *args, **options):
        # self.customer_update()
        # self.contractor_update()
        # self.product_update()
        self.procurement_update()

