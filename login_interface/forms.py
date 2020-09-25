from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    university_id = forms.CharField(widget=forms.TextInput(), required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'university_id',
            'password1',
            'password2',
        ]
