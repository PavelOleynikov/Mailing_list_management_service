from django.urls import path

from message.apps import MessageConfig
from message.views import (
    MessageCreateView,
    MessageDeleteView,
    MessageListView,
    MessageUpdateView,
)

app_name = MessageConfig.name

urlpatterns = [
    path("message/", MessageListView.as_view(), name="message"),
    path("create_message", MessageCreateView.as_view(), name="create_message"),
    path("update_message/<int:pk>", MessageUpdateView.as_view(), name="update_message"),
    path("delete_message/<int:pk>", MessageDeleteView.as_view(), name="delete_message"),
]
