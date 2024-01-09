from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm

def registration(request):
    context = {
        'title': "registration",
    }

    return render(request, 'users/registration.html', context)
 
def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:   
        form = UserLoginForm()

    context = {
        'title': "Login",
        'form': form
    }

    return render(request, 'users/login.html', context)

def logout(request):
    context = {
        'title': "logout",
    }

    return render(request, '', context)

def profile(request):
    context = {
        'title': "profile",
    }

    return render(request, 'users/profile.html', context)
