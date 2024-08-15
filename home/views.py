from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as auth_login
from .forms import CustomAuthenticationForm

def home(request):
    # Add context for popular writers, highlighted portfolios, etc.
    # context = {
    #     'highlighted_portfolios': [],  # Fetch data here
    #     'recent_articles': [],  # Fetch data here
    # }
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(f'/user/{user.username}')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def singup(request):
    return render(request, 'singup.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def user_redirect(username):
    return redirect('user_page', username=username)