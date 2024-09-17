from django.shortcuts import render, redirect
from django.contrib.auth import logout, login as auth_login
from .forms import CustomAuthenticationForm, SignUpForm
from articles.models import Article

def home(request):
    
    latest_articles = Article.objects.order_by('-created_at')[:15]

    return render(request, 'home.html', {
        'latest_articles': latest_articles,
    })

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def user_redirect(username):
    return redirect('user_page', username=username)