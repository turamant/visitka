from django import forms
from .models import ContactRequest
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = self.instance.user.email
