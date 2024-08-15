from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("login", views.login, name='login'),
    path("singup", views.singup, name='singup'),
    path("logout/", views.logout_view, name='logout'),
    path("user/<str:username>/", views.user_redirect, name='user_redirect'),
]