from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(f'/login/user/{user.username}')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def user_page(request, username):
    return render(request, 'user_page.html', {'username': username})

def logout_view(request):
    logout(request)
    return redirect('/login/')