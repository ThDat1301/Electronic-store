from home_page.models import Category
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse


def get_category(request):
    categories = Category.objects.all()
    data = {
        'categories': categories,
    }
    return data


def add_To_Cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    image = request.POST.get('image')
    quantity = request.POST.get('quantity')
    if id in cart:
        cart[id]['quantity'] = int(cart[id]['quantity']) + 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'image': image,
            'quantity': quantity
        }
    request.session['cart'] = cart
    return JsonResponse({'cart': request.session['cart'], 'totalitems':len(request.session['cart'])})


def delete_from_cart(request):
    pId = request.POST.get('id')
    cart = request.session['cart']
    del cart[pId]
    request.session['cart'] = cart
    total = 0
    if 'cart' in request.session:
        for key, value in request.session['cart'].items():
            total += float(value['price']) * float(value['quantity'])
    else:
        request.session['cart'] = {}
    return render(request, 'cart.html', {
        'cart': request.session['cart'],
        'totalitems': len(request.session['cart']),
        'total': total
    })


def reduce_From_Cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    image = request.POST.get('image')
    quantity = request.POST.get('quantity')
    if id in cart:
        cart[id]['quantity'] = int(cart[id]['quantity']) - 1
        if cart[id]['quantity'] < 1:
            del cart[id]
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'image': image,
            'quantity': quantity
        }
    request.session['cart'] = cart
    return JsonResponse({'cart': request.session['cart'], 'totalitems': len(request.session['cart'])})





