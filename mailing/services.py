import datetime

from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing, MailingAttempt



def send_mailing(mailing):
    report = []

    mailing.status_ending = Mailing.STATUS_STARTED
    mailing.save()

    for recipient in mailing.recipients.all():
        try:
            send_mail(
                subject=mailing.message.theme,
                message=mailing.message.body,
                recipient_list=[recipient.email],
                from_email=settings.DEFAULT_FROM_EMAIL,
                fail_silently=False,
            )

            MailingAttempt.objects.create(
                mailing=mailing,
                status='successful',
                server_response='Электронное письмо успешно отправлено',
            )

        except Exception as e:
            MailingAttempt.objects.create(
                mailing=mailing,
                status='unsuccessful',
                server_response=str(e),
            )
            report.append(
                f"{datetime.datetime.now()} - {recipient.email} ошибка - {str(e)}"
            )

    mailing.status_ending = Mailing.STATUS_COMPLETED
    mailing.status_mail = "\n".join(report)
    mailing.save()
    