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