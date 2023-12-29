from django.shortcuts import render

def catalog(request):
    goods = [
        {'price':100,'name': 'Sima', 'image': 'asdasd'},
        {'price':100,'name': 'Sima', 'image': 'asdasd'},
        {'price':100,'name': 'Sima', 'image': 'asdasd'},

        
             ]
    return render(request,'goods/catalog.html', goods)


def product(request):
    return render()