from django import forms
from .models import CustomerMessage


class CustomerMessageForm(forms.ModelForm):

    class Meta:
        model = CustomerMessage
        fields = ('reason', 'user_msg',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_msg'].label = 'Message'
