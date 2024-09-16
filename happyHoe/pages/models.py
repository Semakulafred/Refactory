from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=400)
    inStock = models.IntegerField()
    price = models.IntegerField(default=0,)
    brand = models.CharField(max_length=60)
    image = models.ImageField( upload_to='uploads/products', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'products'
    
    
class Customer(models.Model):
    Customername = models.CharField(max_length=100)
    customeradress = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.Customername

class Sale(models.Model):
    productname = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    totalprice = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return self.productname


