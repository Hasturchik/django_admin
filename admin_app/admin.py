from django.contrib import admin
from .models import Station, Page, Service, Setting

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'address', 'description', 'latitude', 'longitude',)
    search_fields = ('name', 'number', 'address',)
    list_filter = ('name',)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title_ru', 'title_en', 'content_ru', 'content_en',)
    search_fields = ('url', 'title_ru', 'title_en',)
    list_filter = ('content_ru', 'content_en',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('icon_class', 'cost', 'sorting_order', 'status',)
    search_fields = ('icon_class', 'status',)
    list_filter = ('status',)

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value',)
    search_fields = ('key',)