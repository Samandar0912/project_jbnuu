from django.shortcuts import render, get_object_or_404
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


def newsDetail(request, pk):
    News = get_object_or_404(post_site_news, pk=pk)
    other_news = post_site_news.objects.exclude(pk=pk)[:5]
    context = {
        'postNews': News,
        'other_news':other_news
    }
    return render(request, 'news/newsDetail.html', context)



def postAnnouns(request):
    Announs = post_site_elon.objects.all()
    context = {
        'postAnnouns':Announs
    }
    return render(request, 'news/announs.html', context)


def elonDetail(request, pk):
    elon = get_object_or_404(post_site_elon, pk=pk)
    other = post_site_elon.objects.exclude(pk=pk)[:5]
    context = {
        'postElon': elon,
        'elonlar':other
    }
    return render(request, 'news/elonDetail.html', context)


def flial(request):
    return render(request,'flial/flial.html')

def univerHaqida(request):
    return render(request,'flial/universitet_haqida.html')

def univerHaqidaDetail(request):
    return render(request,'flial/universitet-haqida/universitet-haqida_detail.html')



def fakultet(request):
    return render(request,'flial/fakultet.html')

def markazlar(request):
    return render(request,'flial/markazlar.html')

def markaz_detail(request):
    return render(request,'flial/markazlar/markaz_detail.html')

def jobs(request):
    return render(request,'flial/jobs.html')

def rekvezit(request):
    return render(request,'flial/Rekvizitlar.html')


def raxbariyat(request):
    return render(request,'flial/raxbariyat.html')


def history(request):
    return render(request,'flial/history.html')


def struktura(request):
    return render(request,'flial/struktura.html')

def tuzulma(request):
    return render(request, 'flial/struktura.html')