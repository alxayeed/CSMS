from django.urls import path
from . import views

urlpatterns = [
path('', views.index,name='index'),
path('login/', views.login,name='Employe login'),
path('logout/', views.logout,name='Employe logout'),

]