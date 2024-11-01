from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin


# Categorya fakultet uchun ################################################

class Category_facultet(models.Model):
    title = models.CharField(max_length=250, verbose_name="Fakultet nomi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan sanasi")
    
    def __str__(self):
        return str(self.title)

# Categorya fakultet uchun ################################################

class post_site_news(models.Model):
    title = models.CharField(max_length=250, verbose_name="Yangiliklar sarlovhasi")
    body = models.TextField(verbose_name="Yangiliklar tanasi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan sanasi")
    photo = models.ImageField(upload_to='media/news_photo/', max_length=None)   