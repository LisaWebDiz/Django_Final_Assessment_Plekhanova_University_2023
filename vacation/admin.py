from django.contrib import admin

from .models import Villa, Yacht, Vehicle, VillaPhoto, YachtPhoto, VehiclePhoto


class VillaPhotoInline(admin.TabularInline):
    model = VillaPhoto
    extra = 1


@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    inlines = [VillaPhotoInline]
    list_display = ('id', 'title', 'bedrooms_number', 'bathrooms_number', 'sea_distance', 'price_per_day', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price_per_day', 'publication_date')
    list_editable = ('price_per_day', 'exist')
    list_filter = ('exist',)


class YachtPhotoInline(admin.TabularInline):
    model = YachtPhoto
    extra = 1


@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    inlines = [YachtPhotoInline]
    list_display = ('id', 'title', 'cabins_number', 'beds_number', 'maximum_speed', 'price_per_day', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price_per_day', 'publication_date')
    list_editable = ('price_per_day', 'exist')
    list_filter = ('exist',)


class VehiclePhotoInline(admin.TabularInline):
    model = VehiclePhoto
    extra = 1


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehiclePhotoInline]
    list_display = ('id', 'title', 'color', 'seats_number', 'doors_number', 'transmission', 'price_per_day', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price_per_day', 'publication_date')
    list_editable = ('price_per_day', 'color', 'exist')
    list_filter = ('exist',)
