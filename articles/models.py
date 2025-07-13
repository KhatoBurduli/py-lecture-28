from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.EmailField()
    picture = models.ImageField(upload_to="articles/", blank=True, null=True)