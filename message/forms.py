from django.forms import ModelForm

from mailing.models import Message


class MessageForm(ModelForm):
    """ Форма для отправки сообщения """

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for field in self._meta.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Message
        fields = "theme", "body"
