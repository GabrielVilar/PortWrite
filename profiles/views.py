from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import User
from articles.models import Article
from django.contrib import messages
from .models import Profile, WriterRequest
from .forms import EditUserForm, WriterProfileForm, NotificationSettingsForm, ArticleForm

User = get_user_model()

@login_required(login_url='home')
def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    edit_user_form = EditUserForm(instance=user)
    writer_profile_form = WriterProfileForm(instance=profile)
    writer_request_pending = WriterRequest.objects.filter(user=user, is_approved=False).exists()

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
        'writer_request_pending': writer_request_pending,
        'current_url': request.resolver_match.url_name,
    })

@login_required(login_url='home')
def user_settings_view(request, username):
    user = get_object_or_404(User, username=username)

    # Handle password change form
    if request.user == user:
        if request.method == 'POST':
            password_form = PasswordChangeForm(request.user, request.POST)
            notification_form = NotificationSettingsForm(request.POST, instance=request.user)
            
            if 'change_password' in request.POST:
                if password_form.is_valid():
                    user = password_form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Your password was successfully updated!')
                    return redirect('user_settings', username=request.user.username)
                else:
                    messages.error(request, 'Please correct the errors below.')
            elif 'update_notifications' in request.POST:
                if notification_form.is_valid():
                    notification_form.save()
                    messages.success(request, 'Your notification settings were updated!')
                    return redirect('user_settings', username=request.user.username)
        else:
            password_form = PasswordChangeForm(request.user)
            notification_form = NotificationSettingsForm(instance=request.user)
    else:
        password_form = None
        notification_form = None

    return render(request, 'user_menu.html', {
        'user': user,
        'form': password_form,
        'notification_form': notification_form,
        'current_url': request.resolver_match.url_name
    })

@login_required(login_url='home')
def user_saved_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'saved_articles.html', {'user': user})

@login_required(login_url='home')
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

@login_required(login_url='home')
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

@login_required(login_url='home')
def user_create_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    
    # Ensure the user is a writer before allowing article creation
    if not user.is_writer:
        messages.error(request, "You need to be a writer to create an article.")
        return redirect('user_profile', username=user.username)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            
            # Associate the article with the current writer user
            article.writer = user
            
            # Get the plain text content from the hidden field
            #final_content = request.POST.get('final_content', '').strip()
            #article.content = final_content  # Save only the plain text content
            
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()  # Display an empty form for GET requests

    return render(request, 'create_articles.html', {
        'user': user,
        'article_form': form,
        'current_url': request.resolver_match.url_name
    })

@login_required(login_url='home')
def user_articles_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_articles.html', {'user': user})

def writer_profile_view(request, username):
    writer = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=writer)
    
    # Get all articles by this writer
    articles = Article.objects.filter(writer=writer)
    
    context = {
        'writer': writer,
        'profile': profile,
        'articles': articles,  # Pass the articles to the template
    }
    return render(request, 'writer_page.html', context)

@login_required(login_url='home')
def request_writer(request, username):
    user = get_object_or_404(User, username=username)
    if not user.is_writer:
        # Check if a request has already been made
        if not WriterRequest.objects.filter(user=user).exists():
            WriterRequest.objects.create(user=user)
            messages.success(request, "Your request to become a writer has been submitted.")
        else:
            messages.info(request, "You have already submitted a request.")
    return redirect('user_profile', username=username)

@login_required(login_url='home')
def user_admin_page_view(request, username):
    user = get_object_or_404(User, username=username)
    if not user.is_administrator:
        return redirect('home')  # Only administrators can access this page
    
    writer_requests = WriterRequest.objects.filter(is_approved=False)
    
    return render(request, 'user_menu.html', {
        'user': user,
        'writer_requests': writer_requests,
        'current_url': request.resolver_match.url_name
    })

@login_required(login_url='home')
def approve_writer(request, request_id):
    writer_request = get_object_or_404(WriterRequest, id=request_id)
    if request.user.is_administrator:
        writer_request.user.is_writer = True
        writer_request.is_approved = True
        writer_request.user.save()
        writer_request.save()
        messages.success(request, f"{writer_request.user.username} has been approved as a writer.")
    return redirect('adm_page', username=request.user.username)