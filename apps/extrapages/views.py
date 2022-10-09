from django.shortcuts import render
from apps.extrapages.models import HududiyMarkaz, Rahbar, Boglanish

def hududiy_markazlar(request):
    markazlar = HududiyMarkaz.objects.all()
    return render(request, 'hududiy-markazlar.html', {'markazlar': markazlar})


def rahbarlar(request):
    rahbarlar = Rahbar.objects.all()
    return render(request, 'rahbarlar.html', {'rahbarlar': rahbarlar})

