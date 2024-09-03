from django.shortcuts import render


def article(request):
    return render(request, 'article.html')
