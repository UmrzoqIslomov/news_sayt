from django.shortcuts import render
from .models import Category, Comments
from .models import News
import requests as re


# Create your views here.
def valyuta():
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    return re.get(url).json()


def index(requests):
    ctgs = Category.objects.all().filter(is_name=True)
    news = News.objects.all().order_by("-pk")
    tex_ctg = Category.objects.get(slug='texnologiya')
    texnologiya = News.objects.filter(ctg=tex_ctg).order_by("-pk")
    sportctg = Category.objects.get(slug="sport")
    sport_new = News.objects.filter(ctg=sportctg).order_by("-pk")
    jahon_ctg = Category.objects.get(slug='jahon')
    jahon_news = News.objects.filter(ctg=jahon_ctg).order_by("-pk")
    uzbek_ctg = Category.objects.get(slug='uzbekistan')
    uzbek_news = News.objects.filter(ctg=uzbek_ctg).order_by("-pk")
    game_ctg = Category.objects.get(slug="game_news")
    games_news = News.objects.filter(ctg=game_ctg).order_by("-pk")
    biznes_ctg = Category.objects.get(slug="biznes")
    biznes_news = News.objects.filter(ctg=biznes_ctg).order_by("-pk")

    ctx = {
        "ctgs": ctgs,
        "valyuta": valyuta,
        "news": news,
        "texnologiya": texnologiya,
        "sport_new": sport_new,
        "jahon_news": jahon_news,
        "uzbek_news": uzbek_news,
        "games_news": games_news,
        "biznes_news": biznes_news,
    }
    return render(requests, "index.html", ctx)


def category(requests, slug):
    ctgs = Category.objects.all()
    ctg = Category.objects.get(slug=slug)
    news = News.objects.filter(ctg_id=ctg.id).order_by("-pk")

    ctx = {
        "ctgs": ctgs,
        "valyuta": valyuta,
        "ctg": ctg,
        "news": news
    }
    return render(requests, "category.html", ctx)


def contact(requests):
    ctgs = Category.objects.all()
    ctx = {
        "ctgs": ctgs,
        "valyuta": valyuta
    }
    return render(requests, "contact.html", ctx)


def search(requests):
    ctgs = Category.objects.all()

    ctx = {
        "ctgs": ctgs,
        "valyuta": valyuta
    }
    return render(requests, "search.html", ctx)


def view(requests, pk):
    print(pk)
    ctgs = Category.objects.all()
    new = News.objects.get(pk=pk)
    news = News.objects.all().order_by('-pk')
    comments = Comments.objects.filter(new=new)
    if requests.POST:
        comment = Comments()
        comment.name = requests.POST.get("name", "")
        comment.text = requests.POST.get("text", "")
        comment.new = new
        comment.save()
    ctx = {
        "ctgs": ctgs,
        "valyuta": valyuta,
        "comments": comments,
        "new": new,
        "news": news,

    }
    return render(requests, "view.html", ctx)

