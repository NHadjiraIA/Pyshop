from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Product, Fruit, Vegetable

def index(request):
    products = Product.objects.all()
    return render(request,'index.html',
                  {'products': products})

def fruit(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruits.html',
                  {'fruits': fruits})

def vegetable(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'vegetables.html',
                  {'vegetables': vegetables})

def new(request):
    return HttpResponse('This is new product')

