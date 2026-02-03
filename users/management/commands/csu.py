from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Добавление тестового суперюзера"

    def handle(self, *args, **options):
        managers_group, created = Group.objects.get_or_create(name="Менеджеры")
        if created:
            permissions = Permission.objects.filter(
                codename__in=["add_product", "change_product"]
            )
            managers_group.permissions.set(permissions)

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
                user: User = User.objects.create(
                    email=data_user["email"],
                    is_staff=data_user["is_staff"],
                    is_active=data_user["is_active"],
                    is_superuser=data_user["is_superuser"],
                )
                user.set_password(data_user["password"])
                user.save()

                if not data_user["is_superuser"]:
                    user.groups.add(managers_group)
