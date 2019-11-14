from django.urls import path
from . import views

urlpatterns = [
path('', views.index,name='index'),
path('login/', views.login,name='Employe login'),
path('logout/', views.logout,name='Employe logout'),
path('order-list/', views.viewOrderList,name='Employe Order List'),
path('order-details/<order_id>', views.viewOrderDetails,name='Employe Order Details'),
path('order-confirm/<order_id>/',views.orderConfirmation,name='Employe Order Confirmation'),
]