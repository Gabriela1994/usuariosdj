from django.urls import path
from . import views


app_name = "users_app"

urlpatterns = [
    path(
        'register/',
        views.UserRegisterView.as_view(),
        name="user_register"
        ),
    path(
        'login/',
        views.Login.as_view(),
        name="user_login"
        ),
    path(
        'logout/',
        views.Logout.as_view(),
        name="user_logout"
        ),
    path(
        'update/',
        views.ChangePasswordView.as_view(),
        name="user_update"
        ),
]
