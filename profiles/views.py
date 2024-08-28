from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required
def user_page(request, username):
    context = {'username': username}
    return render(request, 'user_page.html', context)

User = get_user_model()

def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_page.html', {'user': user})