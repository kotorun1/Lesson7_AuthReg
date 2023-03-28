from django.urls import path

from .views import manufacturer_create, manufacturer_list, manufacturer_update, manufacturer_delete, country_create, country_list, country_update, country_delete, product_create, product_list, product_update, product_delete, cart_create, cart_list, cart_update, cart_delete, order_create, order_list, order_update, order_delete

urlpatterns = [
    path('manufacturer/create/', manufacturer_create, name='manufacturer_create'),
    path('manufacturer/list/', manufacturer_list, name='manufacturer_list'),
    path('manufacturer/update/<int:pk>/', manufacturer_update, name='manufacturer_update'),
    path('manufacturer/delete/<int:pk>/', manufacturer_delete, name='manufacturer_delete'),
    path('country/create/', country_create, name='country_create'),
    path('country/list/', country_list, name='country_list'),
    path('country/update/<int:pk>/', country_update, name='country_update'),
    path('country/delete/<int:pk>/', country_delete, name='country_delete'),
    path('product/create/', product_create, name='product_create'),
    path('product/list/', product_list, name='product_list'),
    path('product/update/<int:pk>/', product_update, name='product_update'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),
    path('cart/create/', cart_create, name='cart_create'),
    path('cart/list/', cart_list, name='cart_list'),
    path('cart/update/<int:pk>/', cart_update, name='cart_update'),
    path('cart/delete/<int:pk>/', cart_delete, name='cart_delete'),
    path('order/create/', order_create, name='order_create'),
    path('order/list/', order_list, name='order_list'),
    path('order/update/<int:pk>/', order_update, name='order_update'),
    path('order/delete/<int:pk>/', order_delete, name='order_delete'),
]
