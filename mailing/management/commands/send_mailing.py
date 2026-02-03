from django.core.management.base import BaseCommand

from mailing.models import Mailing
from mailing.services import send_mailing

class Command(BaseCommand):
    """ Отправка рассылки """

    help = 'Отправить рассылку'

    def add_arguments(self, parser):

        parser.add_argument('mailing_id', type=int)

    def handle(self, *args, **kwargs):
        mailing_id = kwargs['mailing_id']
        mailing = Mailing.objects.get(id=mailing_id)
        send_mailing(mailing)
        self.stdout.write(self.style.SUCCESS(f'Успешно отправленное почтовое отправление {mailing_id}'))
