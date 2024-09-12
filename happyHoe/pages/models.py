from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=400)
    inStock = models.IntegerField()
    price = models.IntegerField()
    brand = models.CharField(max_length=60)
    image = models.TextField(max_length=5112)

    def __str__(self):
        return self.name
