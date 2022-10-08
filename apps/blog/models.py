from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post-images/')
    featured = models.BooleanField(default=False)
    content = RichTextField()
    description = models.CharField(max_length=200)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'