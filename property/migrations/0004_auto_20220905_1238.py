# Generated by Django 2.2.24 on 2022-09-05 09:38

from django.db import migrations


def add_new_building_status(apps, schema_editor):
    """Добавить квартире статус новостройки"""
    Flat = apps.get_model('property', 'Flat')
    new_buildings = Flat.objects.filter(construction_year__gte= 2015).all()
    for flat in new_buildings:
        flat.new_building = True
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    new_buildings = Flat.objects.filter(construction_year__gte= 2015).all()
    for flat in new_buildings:
        flat.new_building = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(
            add_new_building_status,
            move_backward,
        ),
    ]
