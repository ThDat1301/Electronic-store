from django.contrib.auth import authenticate, login as login_process, logout as logout_process
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from home_page.models import Category, Product, User


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
