from django.db import models

APPLICATION_NAME = ('Аренда борда')

class Price(models.Model):
    price_type = (
        ('S', 'Standart'),
        ('P', 'Premium'),
        ('V', 'VIP'),
        ('V+', 'VIP+'),
    )
    type = models.CharField(max_length = 1, choices = price_type, blank=True, default = 'S', verbose_name='Тип цены')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Ценовую категорию'
        verbose_name_plural = 'Ценовая категория'


class Company(models.Model):
    firm_name = models.CharField(max_length = 150, verbose_name = 'Название фирмы')
    phone_number = models.CharField(max_length = 150, verbose_name = 'Номер телефона')
    state = models.ForeignKey('Adress', on_delete=models.SET_NULL, null=True, verbose_name = 'Адрес')
    site = models.CharField(max_length = 150, verbose_name = 'Сайт')

    def __str__(self):
        return self.firm_name

    class Meta:
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'

class Adress(models.Model):
    state = models.CharField(max_length = 70, verbose_name = 'Область')
    city = models.CharField(max_length =  70, verbose_name = 'Город')
    street = models.CharField(max_length = 70, verbose_name = 'Улица')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'   


class Board(models.Model):
    #photo
    type_construction = (
        ('BB', 'Билборд'),
        ('BG', 'Бигборд'),
        ('BL', 'Бэклайт'),
        ('PR', 'Призматрон'),
        ('SC', 'Скролл'),
    )

    type_construction = models.CharField(max_length = 1, choices = type_construction, blank=True, verbose_name='Тип конструкции')
    format = models.CharField(max_length = 25)

    yes_or_no = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    light = models.CharField(max_length = 1, choices = yes_or_no, default = 'N', blank=True, verbose_name='Свет')
    
    def __str__(self):
        return self.type_construction

    class Meta:
        verbose_name = 'Характеристику борда'
        verbose_name_plural = 'Характеристики борда'


class InstanceBoard(models.Model):
    type_construction = models.ForeignKey("Board", on_delete=models.SET_NULL, null = True, verbose_name = 'Борд')
    side_A_B = (
        ('a', 'A'),
        ('b', 'B'),
    )
    side = models.CharField(max_length = 1, choices = side_A_B, default = 'a', blank = True, verbose_name = 'Сторона')
    type = models.ForeignKey("Price", on_delete=models.SET_NULL, null = True, verbose_name = 'Тип конструкции')
    date_on = models.DateField(verbose_name='Период с: ')
    date_off = models.DateField(verbose_name='Период по: ')
    adress = models.ForeignKey("Adress", on_delete=models.SET_NULL, null = True, verbose_name = 'Адрес')

    def __str__(self):
        return self.type_construction

    class Meta:
        verbose_name = 'Экземпляр борда'
        verbose_name_plural = 'Экземпляры борда'