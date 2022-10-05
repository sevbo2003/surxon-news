from django.contrib import admin
from apps.contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'email', 'created_at']
    list_filter = ['full_name', 'phone_number', 'email', 'created_at']
    search_fields = ['full_name', 'phone_number', 'email', 'created_at']
    list_per_page = 50

    class Meta:
        model = Contact