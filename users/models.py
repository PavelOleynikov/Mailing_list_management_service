from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Модель пользователя """

    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите почту"
    )
    avatar = models.ImageField(
        upload_to="avatar/", blank=True, null=True, verbose_name="Аватар"
    )
    phone_number = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Номер телефона"
    )
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="страна"
    )
    token = models.TextField(verbose_name="Токен", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
