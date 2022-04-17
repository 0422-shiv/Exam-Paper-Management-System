from django import forms
from .models import SendNotification


class SendNotificationForm(forms.ModelForm):
    class Meta:
        model = SendNotification
        fields = ('title','message')