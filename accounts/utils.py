from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError


def send_verification_email(request, user):
    subject = "Verify Your Email"

    scheme = request.scheme
    host = request.get_host()
    verification_link = (
        f"{scheme}://{host}/email_verification/{user.verification_token}/"
    )

    # Email message in plain text
    message = f"""
    Hi {user.username},

    Click the link below to verify your email:

    {verification_link}

    Thank you!
    """

    # HTML version of the email
    html_message = render_to_string(
        "email/verification_email.html",  # Make sure to create this template
        {"user": user, "verification_link": verification_link},
    )

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
            html_message=html_message,  # Sending HTML content as well
        )
    except BadHeaderError:
        print("Invalid header found while sending email.")
