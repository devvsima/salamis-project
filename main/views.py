from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from goods.models import Products
def index(request) -> HttpResponse:
    products = Products.objects.first()
    context = {
        "title": 'Salamis',
        "products": products,
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        "title": 'About us',
    }
    return render(request, 'main/about.html', context)
