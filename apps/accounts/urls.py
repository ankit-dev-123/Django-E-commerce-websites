from django.urls import path
from .views import login_view, register_view, verify_email, logout_view

# URL patterns for user account management (login, register, logout, verify)
urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("verify/<int:user_id>/", verify_email, name="verify_email"),
    path("logout/", logout_view, name="logout"),
]