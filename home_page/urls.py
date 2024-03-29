from django.urls import path, include
from . import views
from . import template_context

urlpatterns = [
    path('', views.index, name='home_page'),
    path('category/<int:cate_id>/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('product/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('add-to-cart', template_context.add_To_Cart, name='add_To_Cart'),
    path('filter_product', views.filter_product, name='filter_product'),
    path('checkout/', views.checkOutWithStripe, name='checkout'),
    path('delete-from-cart', template_context.delete_from_cart, name='delete-from-cart'),
    path('reduce-from-cart', template_context.reduce_From_Cart, name='reduce-from-cart'),
    path('myorder', views.my_order, name='my_order'),
    path('myorder/<int:order_id>/', views.order_detail, name='order_detail')
]