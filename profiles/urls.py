from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('<str:username>/', views.user_profile_view, name='user_profile'),
    path('<str:username>/settings/', views.user_settings_view, name='user_settings'),
    path('<str:username>/saved_articles/', views.user_saved_articles_view, name='saved_articles'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)