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
    path('reciever-order-list/',views.recieverOrderList,name='OrderList forMe'),
    path('reciever-view-order/<post_id>/',views.orderForMe,name='reciever order details'),
    path('order-recieved/<order_id>/',views.order_recieved,name='Order Recieved'),
    path('payment/<order_id>',views.payment,name='payment'),
    path('order-list/',views.order_list,name='order list'),
    path('view-order/<post_id>/',views.order_details,name='order details'),

]
