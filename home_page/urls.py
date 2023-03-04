from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('category/<int:cate_id>/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('product/', views.product_detail, name='product_detail')
#    path('product/<int:prod_id>/', views.product_detail, name='product_detail')
]