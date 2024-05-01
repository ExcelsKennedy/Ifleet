from django import forms
from .models import contact 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['Name', 'Email', 'Message']
        widgets = {
            'Name': forms.TextInput(),
            'Email': forms.EmailInput(),
            'Message': forms.Textarea(),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', 
    }))