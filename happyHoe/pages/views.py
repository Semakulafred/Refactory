from django.shortcuts import render
from pages import views
# Create your views here.

def homePage(request):
    return render(request, 'pages/home.html')

def addProduct(request):
    return render(request, 'addProduct.html')

def recieptPage(request):
    return render(request, 'reciept.html')

def sellPage(request):
    return render(request, 'sell.html')

