from django.contrib import admin
from .models import Category_facultet, post_site_news, post_site_elon, Statistika, MySites, FastLinks, UsefulSites
from django.contrib.auth.models import Group
from django.utils.text import Truncator

# Group modelini admin paneldan olib tashlash
admin.site.unregister(Group)



# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'short_description', 'created']
    list_display_links = ['id', 'short_title']
    
    def short_title(self, obj):
        return Truncator(obj.title).words(3)
    short_title.short_description = 'Title'

    def short_description(self, obj):
        return Truncator(obj.body).words(5)
    short_description.short_description = 'Description'
    
    
    
    
    
class ElonAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'short_description', 'created']
    list_display_links = ['id', 'short_title']
    
    def short_title(self, obj):
        return Truncator(obj.title).words(3)
    short_title.short_description = 'Title'

    def short_description(self, obj):
        return Truncator(obj.body).words(5)
    short_description.short_description = 'Description'
    
    
    
    
    
    
class StatistikaAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'number']
    list_display_links = ['id', 'short_title']
    
    def short_title(self, obj):
        # 'title' maydonini 5 so'zgacha qisqartirish
        return Truncator(obj.title).words(5)
    short_title.short_description = 'Title'
    
    
    
class FastLinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'href']
    list_display_links = ['id', 'short_title']
    
    def short_title(self, obj):
        # 'title' maydonini 5 so'zgacha qisqartirish
        return Truncator(obj.title).words(5)
    short_title.short_description = 'Title'
    
    
    
    
class MySitesAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'href']
    list_display_links = ['id', 'short_title']
    
    def short_title(self, obj):
        # 'title' maydonini 5 so'zgacha qisqartirish
        return Truncator(obj.title).words(5)
    short_title.short_description = 'Title'
    
    
class UsefulSitesAdmin(admin.ModelAdmin):
    list_display = ['id', 'short_title', 'href']
    list_display_links = ['id', 'short_title']
    
    def short_title(self, obj):
        # 'title' maydonini 5 so'zgacha qisqartirish
        return Truncator(obj.title).words(5)
    short_title.short_description = 'Title'
    


admin.site.register(Category_facultet)
admin.site.register(post_site_news, NewsAdmin)
admin.site.register(post_site_elon, ElonAdmin)
admin.site.register(Statistika, StatistikaAdmin)
admin.site.register(FastLinks, FastLinksAdmin)
admin.site.register(MySites, MySitesAdmin)
admin.site.register(UsefulSites, UsefulSitesAdmin)