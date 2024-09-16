from django.shortcuts import render
from pages import views
from .models import Product
# Create your views here.

def homePage(request):
    products = Product.objects.all()
    return render(request, 'pages/home.html', {'products':products})

def addProduct(request):
    return render(request, 'pages/addProduct.html')

def recieptPage(request):
    return render(request, 'pages/reciept.html')

def sellPage(request):
    return render(request, 'pages/sell.html')

