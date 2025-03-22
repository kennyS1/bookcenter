from django.db import models

# Create your models here.
class Book(models):
    bookName = models.CharField(max_length=128)
    picture = models.TextField()
    price = models.IntegerField()
    info = models.TextField()
