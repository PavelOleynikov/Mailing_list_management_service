from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from message.forms import MessageForm
from message.models import Message


@method_decorator(cache_page(60 * 15), name="dispatch")
class MessageListView(LoginRequiredMixin, ListView):
    """ Список сообщений """

    model = Message
    template_name = "message.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.has_perm("message.can_all_view_message"):
            return Message.objects.all()
        return Message.objects.filter(owner=user.pk)


class MessageCreateView(LoginRequiredMixin, CreateView):
    """ Создание сообщения """

    model = Message
    form_class = MessageForm
    template_name = "create_message.html"
    success_url = reverse_lazy("message:message")

    def form_valid(self, form):
        message = form.save(commit=False)
        user = self.request.user
        if user.is_superuser or user.has_perm("message.can_create_message"):
            message.owner = self.request.user
            message.save()
            return super().form_valid(form)
        raise PermissionDenied


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактирование сообщения """

    model = Message
    form_class = MessageForm
    template_name = "update_message.html"
    success_url = reverse_lazy("message:message")

    def form_valid(self, form):
        message = form.save(commit=False)
        user = self.request.user
        if (
            user.is_superuser
            or user.has_perm("message.can_update_message")
            or message.owner == self.request.user
        ):
            message.save()
            return super().form_valid(form)
        raise PermissionDenied


class MessageDetailView(LoginRequiredMixin, DetailView):
    """" Просмотр сообщения """

    model = Message
    template_name = "message/message.html"
    context_object_name = "message"


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление сообщения """

    model = Message
    template_name = "delete_message.html"
    success_url = reverse_lazy("message:message")

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_superuser or user.has_perm("message.can_delete_message"):
            return super().delete(request, *args, **kwargs)
        raise PermissionDenied
