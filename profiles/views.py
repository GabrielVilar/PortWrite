from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import messages
from .models import Profile

@login_required
def user_page(request, username):
    context = {'username': username}
    return render(request, 'user_page.html', context)

User = get_user_model()

def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_page.html', {'user': user})

@login_required
def update_profile_picture(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        if 'remove_picture' in request.POST:

            # Remove the profile picture and set to default
            if profile.profile_picture and profile.profile_picture.name != 'default.png':
                profile.profile_picture.delete(save=False)  # Delete the current image file from storage

            profile.profile_picture = 'default.png'  # Reset to default image
            profile.save()
            messages.success(request, 'Profile picture removed successfully!')

        elif 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            messages.success(request, 'Profile picture updated successfully!')
        else:
            messages.error(request, 'No file selected.')
        
        return redirect('user_profile', username=request.user.username)
    
    return redirect('user_profile', username=request.user.username)