from django.contrib import admin

from .models import Complaint, Flat, Owner


class OwnerInstance(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)

@admin.register(Flat)
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
    raw_id_fields = ('likes',)
    inlines = (OwnerInstance,)



@admin.register(Complaint)
class AdminComplaint(admin.ModelAdmin):
    list_display = (
        'author',
        'flat',
        'text',
    )
    raw_id_fields = (
        'author',
        'flat',
    )

@admin.register(Owner)
class AdminOwner(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phonenumber',
        'pure_phone',
    )
    raw_id_fields = ('flats',)
