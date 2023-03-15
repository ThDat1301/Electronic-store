import json
from urllib import request

from MySQLdb.times import Date
from django.contrib.auth import authenticate, login as login_process, logout as logout_process
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from home_page.models import Category, Product, User, Order, OrderDetail
import stripe
from django.conf import settings
from django.views import View

stripe.api_key = settings.STRIPE_SECRET_KEY



def category(request, cate_id):
    category = Category.objects.get(id=cate_id)
    product = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'category.html', {'category': category, 'product': product})


def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')


def cart(request):
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


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            user = User.objects.create_user(first_name=firstname,
                                            last_name=lastname,
                                            username=username,
                                            email=email,
                                            password=password)
            user.save()
            return redirect('login')
        else:
            messages.error(request, "The password is not the same!")
            redirect('signup')
    return render(request, 'registration/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login_process(request, user)
            return redirect('/')
        else:
            messages.error(request, "User name or password wrong please try again!")
            return redirect('login')
    return render(request, 'registration/login.html')


def logout(request):
    logout_process(request)
    return redirect('login')


def filter_product(request):
    minPrice=request.GET['minPrice']
    maxPrice=request.GET['maxPrice']

    products = Product.objects.all()
    products = products.filter(price__gte=minPrice)
    products = products.filter(price__lte=maxPrice)

    t = render_to_string('ajax/product_list.html', {'product': products})
    return JsonResponse({'data': t})


def checkOutWithStripe(request):
    YOUR_DOMAIN = 'http://127.0.0.1:8000/'
    data = []

    for key, value in request.session['cart'].items():
        data.append(
            {
                'name': value["name"],
                'quantity': value["quantity"],
            }
        )

    for d in data:
        for p in stripe.Product.list(limit=100)["data"]:
            if d["name"] == p["name"]:
                for pr in stripe.Price.list(limit=100)["data"]:
                    if p["id"] == pr["product"]:
                        d['price'] = pr["id"]
                        break
        del d["name"]

    checkout_session = stripe.checkout.Session.create(
        # line_items=[
        #     {
        #         'price': 100,
        #         'quantity': 1,
        #     },
        #     {
        #         'price': 100,
        #         'quantity': 1,
        #     }
        # ],
        line_items=data,
        mode='payment',
        success_url=YOUR_DOMAIN + '',
        cancel_url=YOUR_DOMAIN + '/cart',
    )
    order = Order.objects.create(orderDate=Date.today(),
                                 user_id=request.user.id,
                                 )
    for key, value in request.session['cart'].items():
        order_detail = OrderDetail.objects.create(order_id=order.id,
                                                  product_id=value["id"],
                                                  quantity=value["quantity"],
                                                  price=value["price"])
    del request.session['cart']
    return redirect(checkout_session.url, code=303)


def my_order(request):
    orders = Order.objects.filter(user_id=request.user.id)
    return render(request, 'myorder.html', {'orders': orders})


def order_detail(request, order_id):
    order_detail = OrderDetail.objects.filter(order_id=order_id)
    query = OrderDetail.objects.filter(order_id=order_id).select_related('product')
    products = []
    total_price = 0
    for product in query:
        products.append({
            'id': product.product.id,
            'name': product.product.name,
            'image': product.product.image,
            'quantity': product.quantity,
        })
        total_price += product.product.price * product.quantity

    return render(request, 'orderdetail.html',
                  {'order_detail': order_detail,
                   'products': products,
                   'total_price': total_price},
                  )

