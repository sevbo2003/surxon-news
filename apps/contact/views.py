from django.shortcuts import render
from apps.contact.models import Contact
from apps.contact.forms import ContactForm
from apps.extrapages.models import Boglanish


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_informations(request):
    try:
        contact = Boglanish.objects.get(id=1)
    except:
        contact = None
    return render(request, 'contact_informations.html', {'contact': contact})