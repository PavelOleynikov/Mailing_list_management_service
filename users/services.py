import secrets

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def generate_token():
    return secrets.token_urlsafe(32)


def send_activation_email(host, user, token):
    user.activation_token = token
    user.save()

    mail_subject = "Активация вашего аккаунта"
    message = f"http://{host}/users/token/" + token
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )
    