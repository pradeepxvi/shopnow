from django.core.mail import send_mail

from .models import CustomUser
from django.conf import settings


def send_verification_email(user):
    subject = "Verify Your Email"
    verification_link = (
        f"http://127.0.0.1:8000/email_verification/{user.verification_token}/"
    )

    message = f"""
    Hi {user.username},

    Click the link below to verify your email:

    {verification_link}

    Thank you!
    """

    send_mail(
        subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False
    )
