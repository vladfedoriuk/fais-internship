from django import forms
from django.core.exceptions import ValidationError
import datetime

class DownloadForm(forms.Form):
    
    valid_from = forms.DateTimeField(
        required=True,
        widget=forms.widgets.HiddenInput(
            attrs={
                'type': 'hidden'
            }
        )
    )
    valid_to = forms.DateTimeField(
        required=True,
        widget=forms.widgets.HiddenInput(
             attrs={
                'type': 'hidden'
            }
        )
    )
    version = forms.IntegerField(
        required=True,
        widget=forms.widgets.HiddenInput(
             attrs={
                'type': 'hidden'
            }
        )
    )
    