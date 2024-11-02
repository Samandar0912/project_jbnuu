from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse



# Categorya fakultet uchun ################################################

class Category_facultet(models.Model):
    title = models.CharField(max_length=250, verbose_name="Fakultet nomi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan sanasi")
    
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    
    class Meta:
        verbose_name="Yangilik"
        verbose_name_plural="Yangiliklar"

# YANGILIKLAR UCHUN ################################################

class post_site_news(models.Model):
    title = models.CharField(max_length=250, verbose_name="Yangiliklar sarlovhasi")
    body = models.TextField(verbose_name="Yangiliklar tanasi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan sanasi")
    photo = models.ImageField(upload_to='media/news_photo/', max_length=None)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Yangilik"
        verbose_name_plural="Yangiliklar"

# E'LONLAR UCHUN ################################################

class post_site_elon(models.Model):
    title = models.CharField(max_length=250, verbose_name="E'lon sarlovhasi")
    body = models.TextField(verbose_name="E'lon tanasi")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan sanasi")
    photo = models.ImageField(upload_to='media/elon_photo/', max_length=None)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="E'lon"
        verbose_name_plural="Elonlar"





class Statistika(models.Model):
    title = models.CharField(max_length=150, verbose_name="Ko'rsatgichlar nomi")
    number = models.IntegerField(verbose_name="Ko'rsatgichlar qiymati") 

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name="Asosiy Ko'rsatgichlar"
        verbose_name_plural="Asosiy Ko'rsatgichlar"
