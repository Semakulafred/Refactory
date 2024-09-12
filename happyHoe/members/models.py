from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField( max_length=100, blank=False, null=False)
    user_email= models.EmailField( max_length=254, blank=False, null=False)
    password = models.CharField((""), max_length=50)



def __str__(self):
    return self.name

