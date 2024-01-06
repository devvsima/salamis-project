from django.shortcuts import render

def registration(request):
    context = {
        'title': "registration",
    }

    return render(request, 'users/registration.html', context)
 
def login(request):
    context = {
        'title': "Login",
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
