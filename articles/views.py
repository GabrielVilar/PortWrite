from django.shortcuts import render, get_object_or_404
from articles.models import Article

def article(request):
    return render(request, 'article.html')

def article_detail_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles.html', {'article': article})