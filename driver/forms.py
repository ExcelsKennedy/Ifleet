from django import forms
from .models import DriverProfile, Inspection
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email'] 

class ProfileUpdateForm(forms.ModelForm): 
    class Meta:
        model = DriverProfile  # Corrected model name
        fields = ['image'] 

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', 
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', 
    }))

class inspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['Driver', 'Mirrors', 'Seats', 'Electronics', 'Fuel_level',
        'Damage', 'Medical_kit', 'Body', 'Tires', 'General_Remarks']