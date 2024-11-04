from django.shortcuts import render
from .models import post_site_elon, post_site_news, Statistika

# Create your views here.

def index(request):
    Announs = post_site_elon.objects.all()
    News = post_site_news.objects.all()
    context = {
        'postNews':News,
        'postAnnouns':Announs,
        'statistika':Statistika,
    }
    return render(request, '__index.html', context)


def postNews(request):
    News = post_site_news.objects.all()
    context = {
        'postNews':News
    }
    return render(request, 'news/news.html', context)


def postAnnouns(request):
    Announs = post_site_elon.objects.all()
    context = {
        'postAnnouns':Announs
    }
    return render(request, 'news/announs.html', context)