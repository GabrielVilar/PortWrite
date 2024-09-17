from django import forms
from .models import User
from .models import Profile
from articles.models import Article
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
        widget=forms.Textarea(attrs={'rows': 5, 'maxlength': 2036}),
        required=True,
        label="Biografia",
        help_text="Write a short biography (max 2036 characters)."
    )
    
    instagram = forms.URLField(
        required=False, 
        label="Instagram",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link do Instagram'
        })
    )

    linkedin = forms.URLField(
        required=False, 
        label="LinkedIn",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link do Linkedin'
        })
    )

    facebook = forms.URLField(
        required=False, 
        label="Facebook",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link do Facebook'
        })
    )

    youtube = forms.URLField(
        required=False, 
        label="YouTube",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link do Youtube'
        })
    )

    tiktok = forms.URLField(
        required=False, 
        label="TikTok",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link do Tiktok'
        })
    )

    github = forms.URLField(
        required=False, 
        label="GitHub",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Link do GitHub'
        })
    )
    
    class Meta:
        model = Profile
        fields = ['biography', 'instagram', 'linkedin', 'facebook', 'youtube', 'tiktok', 'github']
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
    }))

    new_password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
    }))

    new_password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
    }))
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class NotificationSettingsForm(forms.ModelForm):
    notifications = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
        label="Receive email notifications"
    )
    class Meta:
        model = User
        fields = ['notifications']

class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escreva aqui o titulo do seu artigo'
        })
    )

    cover_image = forms.ImageField(required=False)

    cover_image_subtitle = forms.CharField(
        required=False,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escreva aqui a legenda da imagem se necessário'
        })
    )

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escreva o conteúdo do artigo'
        })
    )

    images = forms.ImageField(required=False)

    subtitle = forms.CharField(
        required=False,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite aqui a legenda da imagem se necessario'
        })
    )

    video = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file'
        })
    )

    video_url = forms.URLField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'URL do vídeo (YouTube, Vimeo, etc.)'
        })
    )

    class Meta:
        model = Article
        fields = ['title', 'cover_image', 'cover_image_subtitle', 'content','images','subtitle','video','video_url']