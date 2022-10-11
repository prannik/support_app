from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL


def send_email(title: str, body: str, email: str) -> None:
    send_mail(
        title,
        body,
        None,
        (email, ),
        fail_silently=True,
    )
