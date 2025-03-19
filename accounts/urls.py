from django.urls import path
from .views import *
from django.urls import reverse_lazy

from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path("signup/", Signup.as_view(), name="signup"),
    path("signin/", Signin.as_view(), name="signin"),
    path("profile/<str:username>/", Profile.as_view(), name="profile"),
    #
    # email verification url
    path(
        "email_verification/<uuid:token>/",
        email_verification,
        name="email_verification",
    ),
    path("logout/", Logout, name="logout"),
    #
    # password change view
    path(
        "password_change/",
        PasswordChangeView.as_view(template_name="registrations/password_change.html"),
        name="password_change",
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="registrations/password_change_done.html"
        ),
        name="password_change_done",
    ),
    #
    # password rest
    path(
        "password_reset/",
        PasswordResetView.as_view(template_name="registrations/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        PasswordResetDoneView.as_view(
            template_name="registrations/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="registrations/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="registrations/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
