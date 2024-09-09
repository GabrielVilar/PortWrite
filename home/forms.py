from django import forms
from profiles.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu usuário'
    }))
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=256,
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'})
    )
    full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Authentic username'})
    )
    password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password comfirmation'})
    )

    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'password1', 'password2')
        
        class Meta:
         model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já existe.")
        return username 

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user