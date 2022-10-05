from django.contrib import admin
from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser']
    list_filter = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser']
    list_per_page = 50
