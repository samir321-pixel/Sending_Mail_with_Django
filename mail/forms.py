from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput
from django import forms
from .models import *

class MailForm(forms.ModelForm):
    email = EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    subject = CharField(widget=forms.TextInput(attrs={'placeholder': 'subject'}))
    message = CharField(widget=forms.TextInput(attrs={'placeholder': 'Message'}))


    class Meta:
        model = Mail  #
        fields = '__all__'
