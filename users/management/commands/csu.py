from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
from message.models import Message
from recipients.models import Recipient
from mailing.models import Mailing
from users.models import User


class Command(BaseCommand):
    help = "Добавление тестового суперюзера и группы менеджеров"

    def handle(self, *args, **options):
        # Создаем или получаем группу "Менеджеры"
        managers_group, created = Group.objects.get_or_create(name="Менеджеры")

        if created:
            # Получаем нужные разрешения для всех моделей
            permissions_to_add = []

            # Для модели Message
            message_content_type = ContentType.objects.get_for_model(Message)
            message_permissions = Permission.objects.filter(
                content_type=message_content_type,
                codename__in=[
                    "can_all_view_message",
                    "can_create_message",
                    "can_update_message",
                    "can_delete_message"
                ]
            )
            permissions_to_add.extend(message_permissions)

            # Для модели Recipient
            recipient_content_type = ContentType.objects.get_for_model(Recipient)
            recipient_permissions = Permission.objects.filter(
                content_type=recipient_content_type,
                codename__in=[
                    "can_all_view_recipients",
                    "can_create_recipient",
                    "can_delete_recipient"
                ]
            )
            permissions_to_add.extend(recipient_permissions)

            # Для модели Mailing
            mailing_content_type = ContentType.objects.get_for_model(Mailing)
            mailing_permissions = Permission.objects.filter(
                content_type=mailing_content_type,
                codename__in=[
                    "can_all_view_mailing",
                    "can_create_mailing",
                    "can_update_mailing",
                    "can_delete_mailing"
                ]
            )
            permissions_to_add.extend(mailing_permissions)

            # Добавляем все разрешения в группу
            managers_group.permissions.set(permissions_to_add)

        # Создаем тестовых пользователей
        users_test_data = [
            {
                "email": "admin@admin.com",
                "is_staff": True,
                "is_active": True,
                "is_superuser": True,
                "password": "1234",
            },
            {
                "email": "1@admin.com",
                "is_staff": True,
                "is_active": True,
                "is_superuser": False,
                "password": "1234",
            },
            {
                "email": "2@admin.com",
                "is_staff": True,
                "is_active": True,
                "is_superuser": False,
                "password": "1234",
            },
        ]

        for data_user in users_test_data:
            get_user = User.objects.filter(email=data_user["email"]).first()
            if not get_user:
                user = User.objects.create(
                    email=data_user["email"],
                    is_staff=data_user["is_staff"],
                    is_active=data_user["is_active"],
                    is_superuser=data_user["is_superuser"],
                )
                user.set_password(data_user["password"])
                user.save()

                if not data_user["is_superuser"]:
                    user.groups.add(managers_group)
