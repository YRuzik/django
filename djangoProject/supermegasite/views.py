from django.shortcuts import render
from .models import Product, Category

def index(request):
    return render(request, 'index.html')

def woman(request):
    return render(request, 'woman.html')

def man(request):
    products = Product.objects.all()
    return render(request, 'men.html', {'products': products})

def basket(request):
    return render(request, 'shopingCart.html')

def check_prod(request):
    return render(request, 'checkShoe.html')

def children(request):
    return render(request, 'children.html')



