from django.urls import path
from apps.contact.views import contact, contact_informations


urlpatterns = [
    path('murojat-yuborish/', contact, name='contact'),
    path('boglanish/', contact_informations, name='contact-informations'),
]