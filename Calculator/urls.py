from django.contrib import admin
from django.urls import path, include
from Calculator import views


urlpatterns = [
   path('', views.home, name='home'),
   path('calculate', views.calculate, name='calculate')
]