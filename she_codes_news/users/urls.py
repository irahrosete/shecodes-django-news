from django.urls import path
from .views import CreateAccountView, UpdateAccountView, PasswordChangeCustomView, UserStoryView, UserProfileView


app_name = "users"

urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="createAccount"),
    path("update-account/<str:slug>", UpdateAccountView.as_view(), name="updateAccount"),
    path("password/", PasswordChangeCustomView.as_view(), name="password"),
    path("user-story/<str:slug>", UserStoryView.as_view(), name="userStory"),
    path("profile/<str:slug>", UserProfileView.as_view(), name="profile"),
]