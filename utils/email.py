from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from user_module.models import UserModel


def send_mail(user: UserModel):
    subject = 'welcome to my website'
    code = user.email_active_code
    active_url = f'http://127.0.0.1:8000/active-account/{code}'
    message = f'''
    Hi {user.username}, thank you for registering.
    activate account : {active_url}
                     '''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    email = EmailMessage(subject, message, email_from, recipient_list)
    email.send()