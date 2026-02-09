from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = tuple(n_meta.name for n_meta in Mailing._meta.fields)
