from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pay, name='pay'),
    path('handlerequest/', views.handlerequest, name='HandleRequest'),
]
