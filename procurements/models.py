from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel

from procurements.exceptions import IncorrectArgument, NoSuchId


def get_by_model_and_id(model, _id):
    try:
        _id = int(_id)
    except Exception:
        raise IncorrectArgument()
    try:
        return model.objects.get(id=_id)
    except model.DoesNotExist:
        raise NoSuchId()


class Producer(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование производителя"
    )


class Country(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование страны"
    )


class ProductionType(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование вида продукции"
    )


class ProductType(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование вида товаров"
    )


class OKPD2ProductType(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование вида товаров (ОКПД2)"
    )


class Material(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование материала"
    )


class Colour(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование цвета"
    )


class Characteristic(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование характеристики"
    )
    value = models.FloatField(blank=False, null=True, verbose_name="Значение характеристики")
    measurement = models.CharField(
        max_length=64, blank=False, null=False, verbose_name="Измерение характеристики"
    )


class Product(TimeStampedModel):
    external_id = models.IntegerField(blank=False, null=True, verbose_name="ID товара")
    name = models.TextField(
        blank=False, null=False, verbose_name="Наименование товара"
    )
    producer = models.ForeignKey(
        Producer, blank=False, null=True, verbose_name="Производитель товара",
        on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        Country, blank=False, null=True, verbose_name="Страна происхождения товара",
        on_delete=models.CASCADE
    )
    production_type = models.ForeignKey(
        ProductionType, blank=False, null=True, verbose_name="Вид продукции",
        on_delete=models.CASCADE
    )
    product_type = models.ForeignKey(
        ProductType, blank=False, null=True, verbose_name="Вид товаров",
        on_delete=models.CASCADE
    )
    okpd2_product_type = models.ForeignKey(
        OKPD2ProductType, blank=False, null=True, verbose_name="Вид товаров (ОКПД2)",
        on_delete=models.CASCADE
    )
    characteristics = models.ManyToManyField(
        Characteristic, blank=True, verbose_name="Характеристики"
    )
    material = models.ForeignKey(
        Material, blank=False, null=True, verbose_name="Материал товара",
        on_delete=models.CASCADE
    )
    warranty_period = models.IntegerField(
        blank=False, null=True, verbose_name="Гарантийный срок товара (в днях)"
    )
    colour = models.ManyToManyField(
        Colour, blank=True, verbose_name="Цвет товара"
    )

    # TODO: maybe as property?
    num_of_offers = models.IntegerField(
        blank=False, null=True, verbose_name="Количество действующих оферт"
    )
    sum_of_offers = models.FloatField(
        blank=False, null=True, verbose_name="Сумма в составе контрактов"
    )
    num_of_contracts = models.IntegerField(
        blank=False, null=True, verbose_name="Количество контрактов"
    )


class Region(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Наименование региона"
    )


class BaseUser(TimeStampedModel):
    LEGAL_ENTITY = "legal entity"
    INDIVIDUAL = "individual"
    STATUS = Choices(
        (LEGAL_ENTITY, "юридическое лицо"), (INDIVIDUAL, "физическое лицо")
    )

    inn = models.CharField(
        max_length=64, blank=False, null=True, verbose_name="ИНН заказчика"
    )
    kpp = models.CharField(
        max_length=64, blank=False, null=True, verbose_name="КПП заказчика"
    )
    registration_region = models.ForeignKey(
        Region, blank=False, null=True, verbose_name="Регион регистрации",
        on_delete=models.CASCADE
    )
    num_of_contracts = models.IntegerField(
        blank=False, null=True, verbose_name="Количество контрактов на ПП"
    )
    sum_of_contracts = models.FloatField(
        blank=False, null=True, verbose_name="Сумма контрактов на ПП"
    )
    legal_form = models.CharField(
        max_length=32, choices=STATUS, default=LEGAL_ENTITY,
        verbose_name="Организационно-правовая форма"
    )
    email = models.CharField(
        max_length=64, blank=False, null=True, verbose_name="E-Mail"
    )
    production_types = models.ManyToManyField(
        ProductionType, blank=True, verbose_name="ТОП 3 продукции"
    )


class ContactPerson(TimeStampedModel):
    fio = models.CharField(
        max_length=255, blank=False, null=True, verbose_name="ФИО контактного лица"
    )
    email = models.CharField(
        max_length=255, blank=False, null=True, verbose_name="E-Mail контактного лица"
    )
    phone = models.CharField(
        max_length=64, blank=False, null=True, verbose_name="Телефон контактного лица"
    )


class Customer(BaseUser):
    full_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Полное наименование заказчика"
    )
    short_name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Краткое наименование заказчика"
    )
    contact_person = models.ForeignKey(
        ContactPerson, blank=False, null=True, verbose_name="Контактное лицо",
        on_delete=models.CASCADE
    )

    def get_by_id(self, _id):
        get_by_model_and_id(self, _id)

    def __str__(self):
        return f"Заказчик {self.full_name}"

    class Meta(BaseUser.Meta):
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


class Contractor(BaseUser):
    PLUS = "Yes"
    MINUS = "No"
    STATUS = Choices(
        (PLUS, "Есть"), (MINUS, "Нет")
    )
    REVERSED_STATUS = Choices(
        ("Есть", PLUS), ("Нет", MINUS), ("Да", PLUS)
    )

    external_id = models.IntegerField(blank=False, null=True, verbose_name="ID поставщика")
    name = models.CharField(
        max_length=255, blank=False, null=True, verbose_name="Наименование поставщика"
    )
    phone = models.CharField(
        max_length=64, blank=False, null=True, verbose_name="Телефон организации"
    )
    digital_signature = models.CharField(
        max_length=32, choices=STATUS, default=MINUS, verbose_name="Наличие ЭП\Отсутствие ЭП"
    )
    offer = models.CharField(
        max_length=32, choices=STATUS, default=MINUS, verbose_name="Загружал\не загружал оферты"
    )

    class Meta(BaseUser.Meta):
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class PurchaseMethod(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Способ закупки"
    )


class PurchaseType(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Вид закупки"
    )


class ProductItem(TimeStampedModel):
    product = models.ForeignKey(
        Product, blank=False, null=False, verbose_name="Товар закупки",
        on_delete=models.CASCADE
    )
    quantity = models.BigIntegerField(
        blank=False, null=False, verbose_name="Количество товаров данного вида"
    )
    price = models.FloatField(
        blank=False, null=False, verbose_name="Цена одной единицы товара"
    )


class Law(TimeStampedModel):
    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Название закона"
    )
    text = models.TextField(blank=False, null=True, verbose_name="Текст закона")


class Offer(TimeStampedModel):
    number = models.CharField(
        max_length=255, blank=False, null=False, unique=True, verbose_name="Номер оферты"
    )
    start_date = models.DateTimeField(
        blank=False, null=True, verbose_name="Дата начала действия оферты"
    )
    end_date = models.DateTimeField(
        blank=False, null=True, verbose_name="Дата окончания действия оферты"
    )
    price = models.FloatField(blank=False, null=True, verbose_name="Стимость оферты")


class Contract(TimeStampedModel):
    PLUS = "concluded"
    PLUS2 = "executed"
    MINUS = "terminated"
    ZERO = "refusal"
    INPUT = "data entry"
    STATUS = Choices(
        (PLUS, "Заключен"), (MINUS, "Расторгнут"), (ZERO, "Отказ от заключения"),
        (PLUS2, "Исполнен"), (INPUT, "Ввод сведений")
    )

    registry_number = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Реестровый номер контракта"
    )
    number = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Номер контракта"
    )
    status = models.CharField(
        max_length=32, choices=STATUS, default=PLUS,
        verbose_name="Статус контракта"
    )
    price = models.FloatField(blank=False, null=True, verbose_name="Цена контракта")


class ContractorItem(TimeStampedModel):
    contractor = models.ForeignKey(
        Contractor, blank=False, null=False, verbose_name="Поставщик закупки",
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=255, blank=False, null=True, verbose_name="Адрес поставщика закупки"
    )
    regions = models.ManyToManyField(
        Region, blank=True, verbose_name="Регионы поставки"
    )


class CustomerItem(TimeStampedModel):
    customer = models.ForeignKey(
        Customer, blank=False, null=False, verbose_name="Заказчик закупки",
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=255, blank=False, null=True, verbose_name="Адрес заказчика закупки"
    )


class Purchase(TimeStampedModel):
    PLUS = "took place"
    MINUS = "didn't take place"
    ZERO = "deregistered"
    COMPLETED = "completed"
    CANCELED = "canceled"
    INPUT = "data entry"
    STATUS = Choices(
        (PLUS, "Проведена"), (MINUS, "Не состоялась"), (ZERO, "Снята с публикации"),
        (COMPLETED, "Прием предложений завершен"), (CANCELED, "Отменена"),
        (INPUT, "Ввод сведений")
    )

    name = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Название закупки"
    )
    contractor_item = models.ForeignKey(
        ContractorItem, blank=False, null=True, verbose_name="Поставщик закупки + адрес",
        on_delete=models.CASCADE
    )
    participant_items = models.ManyToManyField(
        CustomerItem, blank=True, verbose_name="Заказчики закупки + их адреса"
    )
    method = models.ForeignKey(
        PurchaseMethod, blank=False, null=True, verbose_name="Способ закупки",
        on_delete=models.CASCADE
    )
    start_date = models.DateTimeField(
        blank=False, null=True, verbose_name="Дата начала торгов"
    )
    end_date = models.DateTimeField(
        blank=False, null=True, verbose_name="Дата конца торгов"
    )
    registry_number = models.CharField(
        max_length=64, blank=False, null=True, verbose_name="Реестровый номер"
    )
    number = models.CharField(
        max_length=255, blank=False, null=True, verbose_name="Номер (?) закупки"
    )
    title = models.TextField(
        blank=False, null=True, verbose_name="Предмет закупки"
    )
    product_items = models.ManyToManyField(
        ProductItem, blank=True, verbose_name="Товары в закупке"
    )
    external_id = models.IntegerField(blank=False, null=True, verbose_name="ID закупки")
    law = models.ForeignKey(
        Law, blank=False, null=True, verbose_name="Закон-основание",
        on_delete=models.CASCADE
    )
    # TODO: add history of price
    price = models.BigIntegerField(blank=False, null=True, verbose_name="Стоимость закупки")
    status = models.CharField(
        max_length=32, choices=STATUS, default=PLUS, verbose_name="Статус закупки"
    )
    url = models.URLField(blank=False, null=True, verbose_name="Ссылка на закупку")
    type = models.ForeignKey(
        PurchaseType, blank=False, null=True, verbose_name="Вид закупки",
        on_delete=models.CASCADE
    )
    offer = models.ForeignKey(
        Offer, blank=False, null=True, verbose_name="Оферта по итогам",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"purchase: {self.name}"

    class Meta:
        verbose_name = "Закупка"
        verbose_name_plural = "Закупки"
