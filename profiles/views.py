from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User
from django.contrib import messages
from .models import Profile
from .forms import EditUserForm

User = get_user_model()

@login_required
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    # If the current logged-in user is the profile owner, allow editing
    if request.user == user:
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully.')
                return redirect('user_profile', username=user.username)  # Reload profile page
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = EditUserForm(instance=user)
    else:
        form = None  # Do not show the form if the user is viewing another user's profile

    return render(request, 'user_menu.html', {
        'user': user,
        'form': form,  # Pass the form to the template
        'current_url': request.resolver_match.url_name
    })

@login_required
def user_settings_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'settings.html', {
        'user': user,
        'current_url': request.resolver_match.url_name
    })

@login_required
def user_saved_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'saved_articles.html', {'user': user})

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

@login_required
def user_edit_view(request, username):
    user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('home')  # Redirect to home page after successful update
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EditUserForm(instance=user)

    return render(request, 'settings.html', {
        'user': user,
        'form': form,
        'current_url': request.resolver_match.url_name
    })