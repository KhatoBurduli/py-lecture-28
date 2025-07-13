from django import forms

from articles.models import Article


# # Create your models here.
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     body = forms.CharField()
#     author = forms.EmailField()

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "author", "picture"]