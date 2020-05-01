from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_number' )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'mobile_number' )
