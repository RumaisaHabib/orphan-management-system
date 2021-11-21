import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail
from django.conf import settings


def send_email(addresses, content, subject):
    send_mail(
        subject,
        content,
        from_email='Deebee4206916@gmail.com',
        recipient_list=addresses,
        fail_silently=False,
    )