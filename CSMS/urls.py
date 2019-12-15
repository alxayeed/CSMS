from django.contrib import admin
from django.urls import path,include
from customer import urls
from Employe import urls
from . import views

admin.site.site_header = "Courier Service Wanagement System"
admin.site.index_title = "Administrator Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('loginPage',views.loginPage,name='loginPage'),
    path('customer/',include('customer.urls')),
    path('employe/',include('Employe.urls')),
]
