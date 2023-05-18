from django.contrib import admin
from .models import Villa, Yacht, Vehicle, VillaPhotos, YachtPhotos, VehiclePhotos# , Category


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}
#
#
# admin.site.register(Category, CategoryAdmin)


class VillaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'bedrooms_number', 'bathrooms_number', 'sea_distance', 'price_per_day', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price_per_day', 'publication_date')
    list_editable = ('price_per_day', 'exist')
    list_filter = ('exist',)


admin.site.register(Villa, VillaAdmin)


class YachtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cabins_number', 'beds_number', 'maximum_speed', 'price_per_day', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price_per_day', 'publication_date')
    list_editable = ('price_per_day', 'exist')
    list_filter = ('exist',)


admin.site.register(Yacht, YachtAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'seats_number', 'doors_number', 'transmission', 'price_per_day', 'exist')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price_per_day', 'publication_date')
    list_editable = ('price_per_day', 'color', 'exist')
    list_filter = ('exist',)


admin.site.register(Vehicle, VehicleAdmin)


admin.site.register(VillaPhotos)
admin.site.register(YachtPhotos)
admin.site.register(VehiclePhotos)



