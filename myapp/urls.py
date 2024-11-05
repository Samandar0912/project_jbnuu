from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('Yangiliklar', postNews, name='news'),
    path("E'lonlar", postAnnouns, name='announs'),
    
    path('Yangiliklar/<int:pk>', newsDetail, name='newsDetail'),
    path("E'lonlar/<int:pk>", elonDetail, name='elonDetail'),

    
]
