# Generated by Django 2.2.24 on 2022-09-05 10:52

from multiprocessing.spawn import old_main_modules

from django.db import migrations


def add_old_building_status(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(
        construction_year__lt=2015,
        new_building=None,
    ).update(new_building=False)
    

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__lt=2015).update(
        new_building=None,
    )

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220905_1238'),
    ]

    operations = [
        migrations.RunPython(
            add_old_building_status,
            move_backward,
        ),
    ]


