from django.urls import path
from . import views
urlpatterns =[
    path("", views.index, name="index"),
    path("1", views.index, name="index"),
    path("<str:pk>", views.news, name="news"),
    path("news/<str:id>", views.spec_news, name="specid"),
    path('scrape/', views.scrape_and_store, name='scrape_and_store'),

]