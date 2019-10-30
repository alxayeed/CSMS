
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.customer_index,name='customer_index'),
    path('sign-up/',views.customer_signup,name='sign up'),
    path('log-in/',views.customer_login,name='log in'),
    path('log-out/',views.customer_logout,name='log out'),
    path('profile/',views.profile,name='profile'),
    path('update-profile/',views.update_profile,name='update profile'),
    path('make-order/',views.make_order,name='make order'),
    path('view-order/',views.view_order,name='view order'),

]
