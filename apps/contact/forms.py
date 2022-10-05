from django import forms
from django import forms
from apps.contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone_number', 'email', 'message', 'file']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingizni kiriting'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon raqamingizni kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Elektron pochtangizni kiriting'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Xabar yozing'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'full_name': 'Ism',
            'phone_number': 'Telefon raqami',
            'email': 'Elektron pochta',
            'message': 'Xabar',
            'file': 'Fayl',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].required = True
        self.fields['phone_number'].required = True
        self.fields['email'].required = True
        self.fields['message'].required = True
        self.fields['file'].required = False

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if len(full_name.split()) < 2:
            raise forms.ValidationError('Ismingizni to\'liq kiriting')
        elif len(full_name) < 10:
            raise forms.ValidationError('Ismingiz kamida 10 ta belgidan iborat bo\'lishi kerak')
        return full_name

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) < 9:
            raise forms.ValidationError('Telefon raqamingiz kamida 9 ta belgidan iborat bo\'lishi kerak')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) < 5:
            raise forms.ValidationError('Elektron pochtangiz kamida 5 ta belgidan iborat bo\'lishi kerak')
        return email

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError('Xabaringiz kamida 10 ta belgidan iborat bo\'lishi kerak')
        return message