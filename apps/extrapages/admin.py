from django.contrib import admin
from apps.extrapages.models import HududiyMarkaz, Rahbar, Boglanish


@admin.register(HududiyMarkaz)
class HududiyMarkazAdmin(admin.ModelAdmin):
    list_display = ['title', 'rahbar', 'manzil', 'qabul', 'telefon', 'email', 'created_at']
    list_filter = ['title', 'rahbar', 'manzil', 'qabul', 'telefon', 'email', 'created_at']
    search_fields = ['title', 'rahbar', 'manzil', 'qabul', 'telefon', 'email', 'created_at']
    list_per_page = 50


@admin.register(Rahbar)
class RahbarAdmin(admin.ModelAdmin):
    list_display = ['title', 'rahbar', 'manzil', 'qabul', 'telefon', 'email', 'created_at']
    list_filter = ['title', 'rahbar', 'manzil', 'qabul', 'telefon', 'email', 'created_at']
    search_fields = ['title', 'rahbar', 'manzil', 'qabul', 'telefon', 'email', 'created_at']
    list_per_page = 50


@admin.register(Boglanish)
class BoglanishAdmin(admin.ModelAdmin):
    list_display = ['manzil', 'telefon', 'faks', 'moljalari', 'avtobuslar', 'link', 'created_at']
    list_filter = ['manzil', 'telefon', 'faks', 'moljalari', 'avtobuslar', 'link', 'created_at']
    search_fields = ['manzil', 'telefon', 'faks', 'moljalari', 'avtobuslar', 'link', 'created_at']
    list_per_page = 5