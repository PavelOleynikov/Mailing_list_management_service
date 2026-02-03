from django.forms import ModelForm

from recipients.models import Recipient


class RecipientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)

        for field in self._meta.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Recipient
        fields = ("email", "full_name", "comments")
