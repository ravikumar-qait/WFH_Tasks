from django.db import models

# Create your models here.


class books(models.Model):
    ISBN = models.IntegerField(primary_key=True)
    title = models.CharField(max_length = 20)
    author = models.CharField(max_length = 20)
    genre = models.CharField(max_length = 10)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.title

