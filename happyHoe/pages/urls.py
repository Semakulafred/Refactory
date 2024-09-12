from django.urls import path
from pages import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('add/', views.addProduct, name='add'),
    

]
