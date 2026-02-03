from django import forms
from django.forms import ModelForm

from mailing.models import Mailing
from recipients.models import Recipient


class MailingForm(ModelForm):
    """ Форма для отправки рассылки """

    recipients = forms.ModelMultipleChoiceField(
        queryset=Recipient.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)

        for field in self._meta.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Mailing
        fields = ["message", "recipients"]


class MailingUpdateForm(ModelForm):
    """ Форма для редактирования рассылки """

    recipients = forms.ModelMultipleChoiceField(
        queryset=Recipient.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
    )

    def clean_recipients(self):

        recipients = self.cleaned_data["recipients"]
        return [r.id for r in recipients]

    def __init__(self, *args, **kwargs):

        super(MailingUpdateForm, self).__init__(*args, **kwargs)
        elems = self.fields
        elems["message"].widget.attrs.update({"class": "form-control"})
        elems["recipients"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Mailing
        fields = ["message", "recipients", "status_ending"]
