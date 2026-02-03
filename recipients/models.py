from django.db import models

from users.models import User


class Recipient(models.Model):
    """" Класс получателей рассылок """

    email = models.EmailField(verbose_name="Почта", help_text="Введите почту")
    full_name = models.CharField(
        max_length=200, verbose_name="ФИО", help_text="Введите ФИО"
    )
    comments = models.TextField(
        verbose_name="Комментарий", help_text="Введите комментарий"
    )
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Получатель"
        verbose_name_plural = "Получатели"

        permissions = [
            ("can_all_view_recipients", "Просмотр всех получателей"),
            ("can_delete_recipient", "Удаление получателя"),
            ("can_create_recipient", "Добавление получателя"),
        ]

    def __str__(self):
        return self.full_name
