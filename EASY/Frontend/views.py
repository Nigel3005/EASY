from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import os


# Create your views here.

def indexView(request):
    data = {
        'page': 'Frontend/home.html',
    }

    return render(request, 'Frontend/index.html', data)


def loginView(request):
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                data = {
                    'page': 'registration/login.html',
                    'error': 'User account not activated',
                }
                return render(request, 'Frontend/index.html', data)
        else:
            data = {
                'page': 'registration/login.html',
                'error': 'Incorrect password and/or username',
            }
            return render(request, 'Frontend/index.html', data)

    data = {
        'page': 'registration/login.html',
        'error': '',
    }

    return render(request, 'Frontend/index.html', data)


def logoutView(request):
    logout(request)
    return redirect('Home')


def handler404(request, *args, **argv):
    if request.get_full_path != f"{os.path}":
        data = {
            'page': 'Frontend/404.html',
        }
        return render(request, 'Frontend/index.html', data)