from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('category/<int:cate_id>/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('logout', views.logout, name='logout')
]