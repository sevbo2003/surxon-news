from django.urls import path
from apps.contact.views import contact


urlpatterns = [
    path('murojat-yuborish/', contact, name='contact'),
]