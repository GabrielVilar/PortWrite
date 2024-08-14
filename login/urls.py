from django.urls import path
from . import views 

urlpatterns = [
    path("", views.login_view, name="login"),
    path("user/<str:username>/", views.user_page, name="user_page"),
    path("logout/", views.logout_view, name="logout"),
]
