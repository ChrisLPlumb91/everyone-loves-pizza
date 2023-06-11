from django import forms
from .models import CustomerMessage


class CustomerMessageForm(forms.ModelForm):

    class Meta:
        model = CustomerMessage
        fields = ('reason', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
