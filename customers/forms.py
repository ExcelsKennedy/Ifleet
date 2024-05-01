from django import forms
from .models import Order, CustomerProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address', 
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', 
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password', 
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', 
    }))

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'location1', 'location2', 'order']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full names'}),
            'location1': forms.TextInput(attrs={'placeholder': 'Where are you now?'}),
            'location2': forms.TextInput(attrs={'placeholder': 'Where is your order going?'}),
            'order': forms.Textarea(attrs={'placeholder': 'What do you want to order'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email'] 

class ProfileUpdateForm(forms.ModelForm): 
    class Meta:
        model = CustomerProfile  # Corrected model name
        fields = ['image'] 
