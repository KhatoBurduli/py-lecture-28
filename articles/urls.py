from django.urls import path

from articles import views


urlpatterns = [
    path('', views.list_articles, name="article-list"),
    path('create/', views.create_article, name="article-create")
]