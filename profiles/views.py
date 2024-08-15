from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_page(request, username):
    context = {'username': username}
    return render(request, 'user_page.html', context)
