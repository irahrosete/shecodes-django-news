from django.urls import path
from .views import CreateAccountView, UpdateAccountView, PasswordChangeCustomView, PasswordChangeDoneCustomView, UserProfileView


app_name = "users"

urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="createAccount"),
    path("update-account/<str:slug>", UpdateAccountView.as_view(), name="updateAccount"),
    path("password/", PasswordChangeCustomView.as_view(), name="password"),
    path("password-done/", PasswordChangeDoneCustomView.as_view(), name="changePasswordDone"),
    path("profile/<str:slug>", UserProfileView.as_view(), name="profile"),
]