from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    class Meta:
        widgets = {
            "username": forms.widgets.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "aria-describedby": "username-help",
                }
            ),
            "password": forms.widgets.PasswordInput(
                attrs={
                    "type": "password",
                    "class": "form-control",
                    "aria-describedby": "password-help",
                }
            ),
        }

    username = forms.CharField(widget=Meta.widgets["username"])
    password = forms.CharField(widget=Meta.widgets["password"])
