from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import CreateView

from mailing.forms import MailingForm, MailingUpdateForm
from mailing.models import Mailing, MailingAttempt
from mailing.services import send_mailing


@method_decorator(cache_page(60 * 15), name="dispatch")
class MailingListView(LoginRequiredMixin, ListView):
    """ Список писем """

    model = Mailing
    template_name = "mailing.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.has_perm("mailing.can_all_view_mailing"):
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    """ Создание письма """

    model = Mailing
    form_class = MailingForm
    template_name = "create_mailing.html"
    success_url = reverse_lazy("mailing:mailing")

    def check_permissions(self):
        user = self.request.user
        if not (user.is_superuser or user.has_perm("mailing.can_create_mailing")):
            raise PermissionDenied

    def form_valid(self, form):
        self.check_permissions()
        mailing: Mailing = form.save(commit=False)
        mailing.owner = self.request.user
        mailing.save()
        form.save_m2m()
        send_mailing(mailing)
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактирование письма """

    model = Mailing
    form_class = MailingUpdateForm
    template_name = "update_mailing.html"
    success_url = reverse_lazy("mailing:mailing")

    def check_permissions(self, mailing):
        user = self.request.user
        if not (
            user.is_superuser
            or user.has_perm("mailing.can_update_mailing")
            or mailing.owner == user
        ):
            raise PermissionDenied

    def form_valid(self, form):
        mailing = form.save(commit=False)
        self.check_permissions(mailing)
        mailing.save()
        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление письма """

    model = Mailing
    template_name = "delete_mailing.html"
    success_url = reverse_lazy("mailing:mailing")

    def check_permissions(self):
        user = self.request.user
        if not (user.is_superuser or user.has_perm("mailing.can_delete_mailing")):
            raise PermissionDenied

    def delete(self, request, *args, **kwargs):
        self.check_permissions()
        return super().delete(request, *args, **kwargs)


class SendMailingView(View):
    """ Отправка письма """

    def post(self, request, mailing_id):
        mailing = get_object_or_404(Mailing, id=mailing_id)
        send_mailing(mailing.id)
        return redirect('mailing_list')


def mailing_attempts_list(request):
    """ Список попыток отправки писем """

    attempts = MailingAttempt.objects.all()

    successful_attempts_count = attempts.filter(status='successful').count()
    unsuccessful_attempts_count = attempts.filter(status='unsuccessful').count()

    context = {
        'attempts': attempts,
        'successful_count': successful_attempts_count,
        'unsuccessful_count': unsuccessful_attempts_count,
    }

    return render(request, 'mailing_attempts_list.html', context)
