from django import forms
from .models import User
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
class EditUserForm(forms.ModelForm):

    full_name = forms.CharField(
        max_length=100,
        required=True,
    )

    username = forms.CharField(
        max_length=64,
        required=True,
    )

    email = forms.EmailField(
        max_length=256,
        required=True,
    )
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('This username is already taken.')
        return username
class WriterProfileForm(forms.ModelForm):
    biography = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'maxlength': 1500}),
        required=True,
        label="Biografia",
        help_text="Write a short biography (max 1500 characters)."
    )
    
    instagram = forms.URLField(
        required=False, 
        label="Instagram",
    )

    linkedin = forms.URLField(
        required=False, 
        label="LinkedIn",
    )

    facebook = forms.URLField(
        required=False, 
        label="Facebook",
    )

    youtube = forms.URLField(
        required=False, 
        label="YouTube",
    )

    tiktok = forms.URLField(
        required=False, 
        label="TikTok",
    )

    github = forms.URLField(
        required=False, 
        label="GitHub",
    )
    
    class Meta:
        model = Profile
        fields = ['biography', 'instagram', 'linkedin', 'facebook', 'youtube', 'tiktok', 'github']
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']