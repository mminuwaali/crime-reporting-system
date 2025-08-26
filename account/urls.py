from . import views
from django.urls import path

app_name = "account"
urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign-in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("sign-out/", views.SignOutView.as_view(), name="sign-out"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("password/", views.PasswordChangeView.as_view(), name="password_change"),
]
