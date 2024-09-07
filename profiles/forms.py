from django import forms
from .models import User
from .models import Profile

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
        max_length=100,
        required=True,
    )

    email = forms.EmailField(
        max_length=254,
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