from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class authors(models.Model):
    author_name = models.CharField(max_length = 20)
    #author_email = models.EmailField(max_length=254,default = None)

    def __str__(self):
        return self.author_name

class genre(models.Model):
    genres = models.CharField(max_length = 20)

    def __str__(self):
        return self.genres


class books(models.Model):
    ISBN = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 20)
    author = models.ForeignKey(authors,default = '-',on_delete=models.SET_DEFAULT)
    genre = models.ForeignKey(genre,default='-',on_delete=models.SET_DEFAULT)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=10)
    issued_by  = models.ForeignKey(User,default = None, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title




