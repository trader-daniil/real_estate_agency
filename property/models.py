from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    """Модель объявление о квартире"""
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
    new_building = models.BooleanField(
        verbose_name='Является ли дом новостройкой',
        null=True,
    )
    likes = models.ManyToManyField(
        User,
        related_name='liked_apartments',
        verbose_name='Пользователи, поставившие лайки',
        blank=True,
    )
    owner_pure_phone = PhoneNumberField(
        blank=True,
        verbose_name='Нормализированный номер телефона владельца',
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    """Модель жалобы на объявление"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='complaints',
        verbose_name='Автор жалобы',
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        related_name='complaints',
        verbose_name='Квартира, на которую пожаловались',
    )
    text = models.TextField(verbose_name='Текст жалобы')

    def __str__(self):
        return (
            f'{self.author.username} пожаловался на '
            f'квартиру по адресу:\n {self.apartment.addres}',
        )


class Owner(models.Model):
    """Модель владельца квартиры"""
    full_name = models.CharField(
        db_index=True,
        max_length=50,
        verbose_name='ФИО владельца',
    )
    owners_phonenumber = models.CharField(
        verbose_name='Номер владельца',
        max_length=20,
    )
    owner_pure_phone = PhoneNumberField(
        blank=True,
        verbose_name='Нормализированный номер телефона владельца',
    )
    flats = models.ManyToManyField(
        Flat,
        related_name='owners',
        verbose_name='Квартиры владельца',
    )
