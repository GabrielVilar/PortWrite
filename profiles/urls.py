from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_profile_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('<str:username>/', views.user_profile_view, name='user_profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)