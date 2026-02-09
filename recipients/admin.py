from django.contrib import admin

from recipients.models import Recipient


@admin.register(Recipient)
class RecipientAdminModel(admin.ModelAdmin):
    list_display = ("email", "full_name", "comments")
