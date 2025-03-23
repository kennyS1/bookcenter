from django.db import models

# Create your models here.
class Book(models.Model):
    bookName = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    info = models.TextField()
