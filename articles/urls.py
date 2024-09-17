from django.urls import path
from . import views 

urlpatterns = [
     path("articles", views.article, name='article'),   
     path('<slug:slug>/', views.article_detail_view, name='article_detail'),
]