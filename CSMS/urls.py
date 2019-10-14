
from django.contrib import admin
from django.urls import path,include
from customer import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
]
