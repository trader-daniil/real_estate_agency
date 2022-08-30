from django.db import models
from django.utils import timezone


class Flat(models.Model):
    owner = models.CharField(
        verbose_name='ФИО владельца',
        max_length=200,
    )
    owners_phonenumber = models.CharField(
        verbose_name='Номер владельца',
        max_length=20,
    )
    created_at = models.DateTimeField(
        verbose_name='Когда создано объявление',
        default=timezone.now,
        db_index=True,
    )
    description = models.TextField(
        verbose_name='Текст объявления',
        blank=True,
    )
    price = models.IntegerField(
        verbose_name='Цена квартиры',
        db_index=True,
    )
    town = models.CharField(
        verbose_name='Город, где находится квартира',
        max_length=50,
        db_index=True,
    )
    town_district = models.CharField(
        verbose_name='Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное',
    )
    address = models.TextField(
        verbose_name='Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4',
    )
    floor = models.CharField(
        verbose_name='Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж',
    )
    rooms_number = models.IntegerField(
        verbose_name='Количество комнат в квартире',
        db_index=True,
    )
    living_area = models.IntegerField(
        verbose_name='количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True,
    )
    has_balcony = models.NullBooleanField(
        verbose_name='Наличие балкона',
        db_index=True,
    )
    active = models.BooleanField(
        verbose_name='Активно-ли объявление',
        db_index=True,
    )
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True,
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'
