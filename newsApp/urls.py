from django.urls import path
from . import views
urlpatterns =[
    path("", views.index, name="index"),
    path("Home", views.index, name="index"),
    path("<str:name>", views.news, name="news"),
    path("news/<str:id>", views.spec_news, name="specid"),
    path('scrape/', views.scrape_and_store, name='scrape_and_store'),

]