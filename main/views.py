from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from mailing.models import Mailing
from message.models import Message
from recipients.models import Recipient


def main_page(request: HttpRequest) -> HttpResponse:
    """ Главная страница """

    user = request.user
    context = {
        "count_message": (
            Message.objects.filter(owner=user).count() if user.is_authenticated else 0
        ),
        "count_mailing": (
            Mailing.objects.filter(owner=user).count() if user.is_authenticated else 0
        ),
        "count_recipients": (
            Recipient.objects.filter(owner=user).count() if user.is_authenticated else 0
        ),
    }

    if user.is_authenticated and user.is_superuser:
        context["count_message"] = Message.objects.count()
        context["count_mailing"] = Mailing.objects.count()
        context["count_recipients"] = Recipient.objects.count()

    return render(request, template_name="base.html", context=context)
