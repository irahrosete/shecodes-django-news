from django.urls import path
from .views import CreateAccountView


pp_name = "users"

urlpatterns = [
    path("create-account/", CreateAccountView.as_view(), name="createAccount"),
]