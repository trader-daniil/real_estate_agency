# Generated by Django 2.2.24 on 2022-09-05 18:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20220905_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_apartments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи, поставившие лайки'),
        ),
    ]
