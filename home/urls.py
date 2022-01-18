from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handleSignUp, name='handleSignUp'),    
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    # path('token', views.token_send, name="token_send"),
    path('success', views.success, name="success"),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('error', views.error_page, name="error"),
]
