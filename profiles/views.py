from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from django.contrib import messages
from .models import Profile
from .forms import EditUserForm, WriterProfileForm

User = get_user_model()

@login_required
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    edit_user_form = EditUserForm(instance=user)
    writer_profile_form = WriterProfileForm(instance=profile)

    added_social_media = {
        'instagram': bool(profile.instagram),
        'linkedin': bool(profile.linkedin),
        'facebook': bool(profile.facebook),
        'youtube': bool(profile.youtube),
        'tiktok': bool(profile.tiktok),
        'github': bool(profile.github),
    }
   
    if request.user == user:
        if request.method == 'POST':
            if 'edit_user_form' in request.POST:
                edit_user_form = EditUserForm(request.POST, instance=user)
                if edit_user_form.is_valid():
                    edit_user_form.save()
                    messages.success(request, 'Your profile has been updated successfully.')
                    return redirect('user_profile', username=user.username)
                else:
                    messages.error(request, 'Please correct the errors below.')

            elif 'writer_profile_form' in request.POST:
                writer_profile_form = WriterProfileForm(request.POST, instance=profile)
                if writer_profile_form.is_valid():
                    writer_profile_form.save()
                    messages.success(request, 'Your writer profile has been updated successfully.')
                    return redirect('user_profile', username=user.username)
                else:
                    messages.error(request, 'Please correct the errors below.')
                    
            elif 'remove_social_media' in request.POST:
                platform = request.POST.get('remove_social_media')
                if platform in ['instagram', 'linkedin', 'facebook', 'youtube', 'tiktok', 'github']:
                    # Set the respective field in the profile to None
                    setattr(profile, platform, '')
                    profile.save()
                    messages.success(request, f'{platform.capitalize()} has been removed successfully.')
                    return redirect('user_profile', username=user.username)
    else:
        edit_user_form = None 
        writer_profile_form = None 
 
    return render(request, 'user_menu.html', {
        'user': user,
        'edit_user_form': edit_user_form,
        'writer_profile_form': writer_profile_form,
        'added_social_media': added_social_media,
        'current_url': request.resolver_match.url_name,
    })

@login_required
def user_settings_view(request, username):
    user = get_object_or_404(User, username=username)

    if request.user == user:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)  # Use the built-in form
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important to prevent logout
                messages.success(request, 'Your password was successfully updated!')
                return redirect('user_settings', username=request.user.username)
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = PasswordChangeForm(request.user)  # Initialize the form with the user
    else:
        form = None  # Do not show the form if the user is viewing another user's profile
        
    return render(request, 'user_menu.html', {
        'user': user,
        'form': form,  # Pass the form to the template
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

@login_required
def user_create_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'create_articles.html', {'user': user})

@login_required
def user_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_articles.html', {'user': user})