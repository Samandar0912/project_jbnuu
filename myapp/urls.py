from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('Yangiliklar', views.postNews, name='news'),
    path("E'lonlar", views.postAnnouns, name='announs'),
    
]
