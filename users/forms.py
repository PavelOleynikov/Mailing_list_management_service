from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации пользователей """

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите email"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Повторите пароль"}
        )


class UserProfileForm(ModelForm):
    """ Форма для изменения профиля пользователя """

    class Meta:
        model = User
        fields = ['email', 'avatar', 'phone_number', 'country']

        def __init__(self, *args, **kwargs):
            super(UserProfileForm, self).__init__(*args, **kwargs)

            self.fields["email"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите email"}
            )

            self.fields["avatar"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Введите пароль"}
            )

            self.fields["phone_number"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Повторите пароль"}
            )
            self.fields["country"].widget.attrs.update(
                {"class": "form-control", "placeholder": "Повторите пароль"}
            )
