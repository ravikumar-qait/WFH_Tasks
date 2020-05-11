from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver



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
    quantity = models.PositiveIntegerField(default=10)
    issued_by  = models.ForeignKey(User,default = None, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title

@receiver(pre_save, sender=books)
def quantity1(sender, instance,*args, **kwargs):
    if instance.quantity != 0:
        instance.available = True
        
@receiver(pre_save, sender=books)
def quantity0(sender, instance,*args, **kwargs):
    if instance.quantity == 0:
        instance.available = False
            

# @receiver(pre_save, sender=books)
# def user_created_sales(sender,instance,*args,**kwargs):
#     if instance.quantity != 0:
#             books.objects.update_or_create(instance.available = False)   