from django.urls import path

from recipients.apps import RecipientsConfig
from recipients.views import (
    RecipientCreateView,
    RecipientDeleteView,
    RecipientDetailView,
    RecipientsListView,
    RecipientUpdateView,
)

app_name = RecipientsConfig.name

urlpatterns = [
    path("", RecipientsListView.as_view(), name="recipients"),
    path("create_recipient/", RecipientCreateView.as_view(), name="create_recipient"),
    path(
        "delete_recipient/<int:pk>/",
        RecipientDeleteView.as_view(),
        name="delete_recipient",
    ),
    path(
        "detail_recipient/<int:pk>/",
        RecipientDetailView.as_view(),
        name="detail_recipient",
    ),
    path(
        "update_recipient/<int:pk>/",
        RecipientUpdateView.as_view(),
        name="update_recipient",
    ),
]
