from django.core.mail import send_mail
from django.conf import settings

# Function that handles sending account verification emails to new users
def send_verification_email(user_obj):
    # Set the subject line for the verification email
    subject = "Verify Your Account"
    # Construct the personalized message body with the user's activation link
    message = f""" Hello {user_obj.username}
    Click this link to verify your account:
    http://127.0.0.1:8000/accounts/verify/{user_obj.id}
    """
    # Sends the email using credentials defined in settings.py
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_obj.email], fail_silently=False)