# Generated by Django 2.2.24 on 2022-09-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220913_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='apartment',
            new_name='flat',
        ),
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='ФИО владельца'),
        ),
    ]
