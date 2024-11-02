from django.contrib import admin
from .models import Category_facultet, post_site_news, post_site_elon

# Register your models here.

admin.site.register(Category_facultet)
admin.site.register(post_site_news)
admin.site.register(post_site_elon)