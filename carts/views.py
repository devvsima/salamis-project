from django.shortcuts import render

def cart_add(request, product_id):
    context = {
        "title": 'Carts',
    }

    return render(request, "", context)

def cart_change(request, product_id):
    context = {
        "title": 'Carts',
    }

    return render(request, "", context)

def cart_remove(request, product_id):
    context = {
        "title": 'Carts',
    }

    return render(request, "", context)
