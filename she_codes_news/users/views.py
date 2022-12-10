from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm, ChangePasswordForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/createAccount.html"

class UpdateAccountView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    context_object_name = "profile"
    slug_field = "username"
    template_name = "users/updateAccount.html"

class PasswordChangeCustomView(PasswordChangeView):
    model = CustomUser
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_change_done')
    template_name = "users/changePassword.html"

class UserStoryView(generic.DetailView):
    model = CustomUser
    context_object_name = "userstory"
    slug_field = "username"
    template_name = "users/userStory.html"

class UserProfileView(generic.DetailView):
    model = CustomUser
    context_object_name = "profile"
    slug_field = "username"
    template_name = "users/userProfile.html"
