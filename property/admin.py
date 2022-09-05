from django.contrib import admin

from .models import Flat


class AdminFlat(admin.ModelAdmin):
    search_fields = (
        'town',
        'town_district',
        'address',
    )
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    readonly_fields = (
        'created_at',
    )
    list_editable = (
        'new_building',
    )
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
    )

admin.site.register(Flat, AdminFlat)
