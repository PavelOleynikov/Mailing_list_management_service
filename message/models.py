from django.db import models

from users.models import User


class Message(models.Model):
    """ Модель для сообщений """

    theme = models.CharField(max_length=150, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма")
    owner = models.ForeignKey(
        User, verbose_name="Владелец письма", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        permissions = [
            ("can_all_view_message", "Просмотр всех сообщений"),
            ("can_delete_message", "Удаление сообщения"),
            ("can_update_message", "Обновление сообщения"),
            ("can_create_message", "Добавление сообщения"),
        ]
