from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import messages
from .models import Profile
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
    
    # Debug: Print initial profile picture state
    logger.debug(f"Initial profile picture: {profile.profile_picture}")
    
    if request.method == 'POST':
        if 'remove_picture' in request.POST:
            # Debug: Log the remove_picture POST request
            logger.debug(f"Received request to remove profile picture for user {request.user.username}")
            
            # Remove the profile picture and set to default
            if profile.profile_picture and profile.profile_picture.name != 'default.png':
                logger.debug(f"Deleting profile picture: {profile.profile_picture}")
                profile.profile_picture.delete(save=False)  # Delete the current image file from storage
            else:
                logger.debug(f"Profile picture is already default or does not exist.")

            profile.profile_picture = 'default.png'  # Reset to default image
            profile.save()
            logger.debug(f"Profile picture set to default for user {request.user.username}")
            messages.success(request, 'Profile picture removed successfully!')
        elif 'profile_picture' in request.FILES:
            # Debug: Log the file upload
            logger.debug(f"Received new profile picture upload for user {request.user.username}")
            
            # Update with the new profile picture
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            logger.debug(f"Profile picture updated to {profile.profile_picture} for user {request.user.username}")
            messages.success(request, 'Profile picture updated successfully!')
        else:
            logger.debug(f"No file selected for upload by user {request.user.username}")
            messages.error(request, 'No file selected.')
        
        # Debug: Log the final state
        logger.debug(f"Final profile picture: {profile.profile_picture}")
        return redirect('user_profile', username=request.user.username)
    
    logger.debug(f"GET request made to update_profile_picture by user {request.user.username}")
    return redirect('user_profile', username=request.user.username)