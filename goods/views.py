from django.shortcuts import render
from goods.models import Categories, Products

def catalog(request, category_slug='all'):
    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)
    
    context ={'products': goods}
    

    return render(request,'goods/catalog.html', context)


def product(request, product_slug=False, product_id=False):
    if product_slug: product = Products.objects.get(slug=product_slug)
    elif product_id: product = Products.objects.get(id=product_id)
    
    context = {'product': product}
    return render(request,'goods/product.html', context)
