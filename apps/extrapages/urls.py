from django.urls import path
from apps.extrapages.views import rahbarlar, hududiy_markazlar


urlpatterns = [
    path('hududiy-markazlar/', hududiy_markazlar, name='hududiy-markazlar'),
    path('rahbariyat/', rahbarlar, name='rahbarlar'),
]