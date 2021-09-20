from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', customer, name='customer'),
    path('add_customer', add_customer, name="add_customer"),
    path('edit_customer/<int:id>', edit_customer, name="edit_customer"),
    path('seller', seller, name='seller'),
    path('add_seller', add_seller, name="add_seller"),
    path('edit_seller/<int:id>', edit_seller, name="edit_seller"),
    path('product', product, name='product'),
    path('add_product', add_product, name="add_product"),
    path('edit_product/<int:id>', edit_product, name="edit_product"),
    path('order', order, name='order'),
    path('add_order', add_order, name="add_order"),
    path('edit_order/<int:id>', edit_order, name="edit_order"),
    path('find_1', find_1, name="find_1"),
    path('find_2', find_2, name="find_2"),
    path('find_3', find_3, name="find_3"),
    path('find_4', find_4, name="find_4"),
    path('find_5', find_5, name="find_5"),
    path('profile_edit/', profile_edit, name="profile_edit"),
    path('admin/', admin.site.urls),
    path('register', register),
    path('login', login),
    path('logout', user_logout),
]