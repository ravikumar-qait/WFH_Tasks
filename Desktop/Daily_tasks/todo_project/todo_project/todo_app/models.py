from django.db import models
from django.utils.timezone import now

# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.item + ' | '+ str(self.completed)


class Deleted(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    deleted_time = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.item + ' | '+ str(self.completed)
    
