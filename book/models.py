from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(default="Book", max_length=100)
    author = models.CharField(default="Auhtor", max_length=100)
    pages_count = models.IntegerField(default=0)