from django.db import migrations


def add_flats_owners_relations(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        owner = Owner.objects.filter(flats__in=[flat]).all().first()
        if not owner:
            owner = Owner.objects.create(
                full_name=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owner_pure_phone=flat.owner_pure_phone
            )
        owner.flats.add(flat)
        owner.save()


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all().iterator():
        owner.flats.clear()
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220913_1425'),
    ]

    operations = [
        migrations.RunPython(
            add_flats_owners_relations,
            move_backward,
        ),
    ]
