from django.shortcuts import render
from apps.contact.models import Contact
from apps.contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def contact_informations(request):
    return render(request, 'contact_informations.html')