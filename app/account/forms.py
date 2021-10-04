from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Form, fields
from django.core.exceptions import ValidationError

from account.models import User


class UserAccountRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image')

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.all().filter(email=email).exists():
            raise ValidationError('Email is already exists')

        return email


class UserAccountProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'image')


class ContactUs(Form):
    subject = fields.CharField(max_length=256, empty_value='Message from TMP')
    message = fields.CharField(widget=forms.Textarea)
