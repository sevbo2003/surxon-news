from django.db import models
from django.core.validators import RegexValidator


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Telefon raqamizni quyidagi ko'rinishda kiriting: '+9989999999'. 15 raqamdan oshmasligi kerak.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    message = models.CharField(max_length=1500)
    file = models.FileField(upload_to='contact-files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Murojat'
        verbose_name_plural = 'Murojatlar'
        ordering = ['-created_at']