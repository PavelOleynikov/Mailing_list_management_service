from django.contrib import admin

from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = tuple(n_meta.name for n_meta in Message._meta.fields)
