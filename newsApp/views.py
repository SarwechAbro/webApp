from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Topic, News, Article
from .web import Web
from newsapi import NewsApiClient
from .news import content

def index(request):
    news = content()

    topics = Topic.objects.all()
   # news = News.objects.all()
    articles = Article.objects.all()
    context = {'topics': topics, 'news': news, 'articles': articles}
    return render(request, "newsApp/index.html", context)


def news(request, name):
    id = Topic.objects.get(name=name)
    news = News.objects.filter(topics=id)
    context = {'news': news, 'topic':name}
    return render(request, "newsApp/news.html", context )

def spec_news(request, id):
     news_item =   get_object_or_404(News, pk=id)
     related_news = News.objects.filter(topics__in=news_item.topics.all()).exclude(id=id)
     context = {'news_item': news_item, 'related_news': related_news }
     return render(request, "newsApp/spec_news.html", context )

def scrape_and_store(request):
    web_instance = Web()
    articles = web_instance.get_articles()

    for article_text in articles:
        News.objects.create(body=article_text)

    return HttpResponse('Articles scraped and stored successfully!')

