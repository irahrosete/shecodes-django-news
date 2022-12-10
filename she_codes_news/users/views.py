from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/createAccount.html"

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
