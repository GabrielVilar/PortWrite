from django.shortcuts import render

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
    return render(request, 'login.html')

def singup(request):
    return render(request, 'singup.html')
