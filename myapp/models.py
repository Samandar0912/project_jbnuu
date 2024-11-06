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
        verbose_name="Categorya"
        verbose_name_plural="Categoryalar"

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
        ordering = ['-id']

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
        ordering = ['-id']




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


class FastLinks(models.Model):
    title = models.CharField(max_length=100, verbose_name='Sayt nomi')
    photo = models.ImageField(upload_to='media/Foydali_Sayt_rasmi/', max_length=None)
    href = models.CharField(max_length=100, verbose_name='Sayt linki')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Tezkor havolalar"
        verbose_name_plural="Tezkor havolalar"
        ordering = ['-id']



class MySites(models.Model):
    title = models.CharField(max_length=100, verbose_name='Sayt nomi')
    photo = models.ImageField(upload_to='media/Foydali_Sayt_rasmi/', max_length=None)
    href = models.CharField(max_length=100, verbose_name='Sayt linki')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Bizni Tizimlar"
        verbose_name_plural="Bizni Tizimlar"
        ordering = ['-id']



class UsefulSites(models.Model):
    title = models.CharField(max_length=100, verbose_name='Sayt nomi')
    photo = models.ImageField(upload_to='media/Foydali_Sayt_rasmi/', max_length=None)
    href = models.CharField(max_length=100, verbose_name='Sayt linki')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Foydali saytlar"
        verbose_name_plural="Foydali saytlar"
        ordering = ['-id']
        
        
        

class UniverHistoryCard(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    body = models.TextField(verbose_name='texti')
    photo = models.ImageField(upload_to='media/photo/', verbose_name='rasm' )
    yil = models.CharField(max_length=9, verbose_name='yilni kiriting')
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Foydali saytlar"
        verbose_name_plural="Foydali saytlar"
        
