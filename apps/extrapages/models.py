from statistics import mode
from django.db import models


class HududiyMarkaz(models.Model):
    title = models.CharField(max_length=200)
    rahbar = models.CharField(max_length=200)
    manzil = models.CharField(max_length=200)
    qabul = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Hududiy Markaz'
        verbose_name_plural = 'Hududiy Markazlar'


class Rahbar(models.Model):
    title = models.CharField(max_length=400)
    rasm = models.ImageField(upload_to = 'rahbariyat/', null=True, blank=True)
    rahbar = models.CharField(max_length=400)
    manzil = models.CharField(max_length=200)
    qabul = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Rahbar'
        verbose_name_plural = 'Rahbariyat'