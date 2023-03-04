from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from home_page.models import Category, Product


def category(request, cate_id):
    category = Category.objects.get(id=cate_id)
    product = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'category.html', {'category': category, 'product': product})


def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())

def product_detail(request):
    template = loader.get_template('product_detail.html')
    return HttpResponse(template.render())
