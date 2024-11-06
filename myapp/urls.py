from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('Yangiliklar', postNews, name='news'),
    path("E'lonlar", postAnnouns, name='announs'),
    
    path('Yangiliklar/<int:pk>', newsDetail, name='newsDetail'),
    path("E'lonlar/<int:pk>", elonDetail, name='elonDetail'),

    path("Filial", flial, name='flial'),
    path("Filial/Universitet-haqida", univerHaqida, name='univerHaqida'),
    path("Filial/Universitet-haqida/univerHaqidaDetail", univerHaqidaDetail, name='univerHaqidaDetail'),
    
    
    path("Filial/Fakultet", fakultet, name='fakultet'),
    path("Filial/Markazlar", markazlar, name='markazlar'),
    path("Filial/Markazlar/RTTM", markaz_detail, name='markaz_detail'),
    
    
    path("Filial/Bo'sh-ish-o'rinlari", jobs, name='jobs'),
    path("Filial/Rekvizitlar", rekvezit, name='rekvezit'),
    
    path("Filial/Raxbariyat", raxbariyat, name='raxbariyat'),
    path("Filial/history", history, name='history'),
    
    path("Filial/Struktura", struktura, name='struktura'),
    
    
    
    
    
]
