from django.shortcuts import render
from .models import Category_facultet, post_site_news, post_site_elon, Statistika, MySites, FastLinks, UsefulSites

# Create your views here.

def index(request):
    Announs = post_site_elon.objects.all()
    News = post_site_news.objects.all()
    mySites = MySites.objects.all()
    fastLinks = FastLinks.objects.all()
    usefulSites = UsefulSites.objects.all()
    statistika = Statistika.objects.all()
    context = {
        'postNews':News,
        'postAnnouns':Announs,
        'statistika':statistika,
        'mySites':mySites,
        'fastLinks':fastLinks,
        'usefulSites':usefulSites,
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