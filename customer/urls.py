
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.customer_index,name='customer_index'),
    path('sign-up/',views.customer_signup,name='sign up'),
    path('log-in/',views.customer_login,name='log in'),
]
