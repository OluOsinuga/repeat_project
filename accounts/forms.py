from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

from .models import CustomUser #custom user has defaults for the field

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        #the fields displayed on admin site
        fields = UserCreationForm.Meta.fields+('username','email','age',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields