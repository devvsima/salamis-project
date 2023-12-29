from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request):
    categoris_all = Categories.objects.all()
    product_all = Products.objects.all()
    result ={'products': product_all,
             'categoris': categoris_all}
    return render(request,'goods/catalog.html', result)


def product(request):
    return render()