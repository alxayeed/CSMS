
from django.contrib import admin
from django.urls import path,include
from customer import urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('sign-up/',views.sign_up,name='sign up'),
    path('customer/',include('customer.urls')),
]
