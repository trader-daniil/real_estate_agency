


def create_owner_from_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        flat_owner, created = Owner.object.get_or_create(full_name=flat.owner)
        flat_owner.flats.add(flat)
        flat_owner.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flats.clear()
        owner.save()



