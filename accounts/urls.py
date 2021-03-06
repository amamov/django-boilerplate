from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login",),
    path("repassword/", views.PasswordChangeView.as_view(), name="password_change",),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
    path("edit/", views.profile_edit, name="profile_edit"),
]
