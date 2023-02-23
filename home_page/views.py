from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def product(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
