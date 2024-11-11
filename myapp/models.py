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


# STATISTIKA UCHUN ################################################


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



# TEZKOR HAVOLALAR UCHUN ################################################

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



# BIZNI TIZIMLAR UCHUN ################################################

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




# FOYDALI SAYTLAR UCHUN ################################################

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
        
        
        
# UNIVERSITET TARIXI UCHUN ################################################

class UniverHistoryCard(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    body = models.TextField(verbose_name='texti')
    photo = models.ImageField(upload_to='media/photo/', verbose_name='rasm' )
    yil = models.CharField(max_length=9, verbose_name='yilni kiriting')
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Universitet Tarixi"
        verbose_name_plural="Universitet Tarixi"
        
        
    
# FLIAL TARIXI UCHUN ################################################

class FilialHistory(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    body = models.TextField(verbose_name='texti')
    photo = models.ImageField(blank=False, upload_to='media/photo/', verbose_name='rasm' )
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Filial Tarixi"
        verbose_name_plural="Filial Tarixi"
        



# FLIAL Tuzulmasi kengashi UCHUN ################################################

class KengashCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    photo = models.ImageField(blank=False, upload_to='media/photo/', verbose_name='rasm' )
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Kengash Kategory"
        verbose_name_plural="Kengash Kategory"
        
        
        
# FLIAL Tuzulmasi kengashi Article UCHUN ################################################

class KengashArticle(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    category = models.ForeignKey(KengashCategory, on_delete=models.CASCADE, related_name="category_kengash")
    photo = models.ImageField(blank=False, upload_to='media/photo/', verbose_name='rasm' )
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name="Kengash Article"
        verbose_name_plural="Kengash Article"
        




# FLIAL Tuzulmasi kengashi Article UCHUN ################################################

class Raxbaryat(models.Model):
    name = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    position = models.CharField(max_length=250, verbose_name="Lavozimi")
    number = models.IntegerField(default=0)
    email = models.EmailField(verbose_name="email", max_length=254)
    photo = models.ImageField(upload_to='media/photo/', verbose_name='rasm' )
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name="Raxbaryat hodmlari"
        verbose_name_plural="Kengash Article"
        






class CategoryCenter(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    photo = models.ImageField(blank=False, upload_to='media/photo/', verbose_name='rasm')

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "Markazlar"
        verbose_name_plural = "Markazlar"


class CenterArticle(models.Model):
    name = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    position = models.CharField(max_length=250, verbose_name="Lavozimi")  # Fixed max_length to be an integer
    number = models.IntegerField(default=0)
    email = models.EmailField(verbose_name="email", max_length=254)
    category = models.ForeignKey(CategoryCenter, on_delete=models.CASCADE, related_name="category_kengash")  # Corrected the ForeignKey reference
    photo = models.ImageField(blank=False, upload_to='media/photo/', verbose_name='rasm')
    body = models.TextField(verbose_name="Markaz Malumotlari")
    
    def __str__(self):
        return str(self.name)  # Changed to self.name instead of self.title
    
    class Meta:
        verbose_name = "Markaz Malumotlari"
        verbose_name_plural = "Markaz Malumotlari"


class Centerplus(models.Model):
    name = models.CharField(max_length=250, verbose_name='Sarlovhasi')
    position = models.CharField(max_length=250, verbose_name="Lavozimi")  # Fixed max_length to be an integer
    category = models.ForeignKey(CenterArticle, on_delete=models.CASCADE)
    photo = models.ImageField(blank=False, upload_to='media/photo/', verbose_name='rasm')
    tg = models.CharField(max_length=100, verbose_name="telegram")
    tell = models.CharField(max_length=100, verbose_name="tell:")
    email = models.EmailField(verbose_name="email", max_length=254)
    insta = models.CharField(max_length=100, verbose_name="Instagram")
    facebook = models.CharField(max_length=100, verbose_name="Facebook")
    
    def __str__(self):
        return str(self.name)  # Changed to self.name instead of self.title
    
    class Meta:
        verbose_name = "Markaz Malumotlari"
        verbose_name_plural = "Markaz Malumotlari"
