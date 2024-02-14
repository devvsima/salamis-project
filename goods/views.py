from django.shortcuts import render
from django.core.paginator import Paginator
from goods.models import Categories, Products
from .utils import q_search
def catalog(request, category_slug=None):
    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None) #search


    # фильтр и поиск
    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    # сортировка
    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)


    paginator = Paginator(goods, 4)
    current_page = paginator.page(int(page))

    context = {
        "products": current_page,
        "slug_url": category_slug,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug=False, product_id=False):
    if product_slug:
        product = Products.objects.get(slug=product_slug)
    elif product_id:
        product = Products.objects.get(id=product_id)

    context = {"product": product}
    return render(request, "goods/product.html", context)
