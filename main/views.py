from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request) -> HttpResponse:
    return render(request, 'index.html', {'sd':1})

def about(request) -> HttpResponse:
    return HttpResponse('about page')