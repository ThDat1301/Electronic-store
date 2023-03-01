from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart')
]