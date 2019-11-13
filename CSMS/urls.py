
from django.contrib import admin
from django.urls import path,include
from customer import urls
from Employe import urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('customer/',include('customer.urls')),
    path('employe/',include('Employe.urls')),
]
