from django.contrib import admin

from .models import Flat, Complaint, Owner


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
        'owners_phonenumber',
        'owner_pure_phone',
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
    raw_id_fields = (
        'likes',
    )

admin.site.register(Flat, AdminFlat)


class AdminComplaint(admin.ModelAdmin):
    list_display = (
        'author',
        'apartment',
        'text',
    )
    raw_id_fields = (
        'author',
        'apartment',
    )

admin.site.register(Complaint, AdminComplaint)


class AdminOwner(admin.ModelAdmin):
    list_display = (
        'full_name',
        'owners_phonenumber',
        'owner_pure_phone',
    )
    raw_id_fields = ('flats',)

admin.site.register(Owner, AdminOwner)
