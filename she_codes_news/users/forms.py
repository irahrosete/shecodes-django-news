from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email"]

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ["username", "email"]

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
