# Generated by Django 2.2.24 on 2022-09-12 13:45

import phonenumbers
from django.db import migrations


def make_phonenumbers_pure(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        if not flat.owners_phonenumber:
            continue
    
        pure_phonenumber = phonenumbers.parse(
            flat.owners_phonenumber,
            'RU',
        )
        if not phonenumbers.is_valid_number(pure_phonenumber):
            continue
        formatted_pure_phonenumber = phonenumbers.format_number(
            pure_phonenumber,
            phonenumbers.PhoneNumberFormat.INTERNATIONAL,
        )
        flat.owner_pure_phone = formatted_pure_phonenumber
        flat.save(update_fields=['owner_pure_phone'])


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        flat.owner_pure_phone = ''
        flat.save(update_fields=['owner_pure_phone'])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220905_2116'),
    ]

    operations = [
        migrations.RunPython(
            make_phonenumbers_pure,
            move_backward,
        ),
    ]
