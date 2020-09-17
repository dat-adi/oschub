from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput())
    email = forms.EmailField(max_length=234, help_text="Please input your university email address.")
    university_id = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'university_id',
            'password1',
            'password2',
        ]
