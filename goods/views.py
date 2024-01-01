from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request):
    # categoris_all = Categories.objects.all()

    goods = Products.objects.all()
    result ={'products': goods}
    
     
    return render(request,'goods/catalog.html', result)


def product(request):
    return render(request,'goods/product.html')
