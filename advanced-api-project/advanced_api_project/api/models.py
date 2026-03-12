from django.db import models
from django.contrib.auth.models import User 

class Author(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    Author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
# Create your models here.
