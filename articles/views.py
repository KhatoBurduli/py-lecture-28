from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Article

def list_articles(request):
    articles = Article.objects.all()
    return render(request, "list_articles.html", {"articles": articles})


def create_article(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # article = Article(**form.cleaned_data )
            # article.save()

            return redirect("article-list")

    return render(request, "create_article.html", {"form":form})