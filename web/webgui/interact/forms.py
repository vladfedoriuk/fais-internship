from django import forms

class ParseForm(forms.Form):
    pass


class ExtractForm(forms.Form):
    
    valid_from_date = forms.DateField(
        required=False,
        label="date from",
        help_text="The date configuration is valid from.",
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'aria-describedby': 'date-from-help'
            }
        )
    )
    
    valid_from_time = forms.TimeField(
        required=False,
        label="time from",
        initial="00:00:00",
        help_text="The time configuration is valid from.",
        widget=forms.widgets.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
                'aria-describedby': 'time-from-help'
            }
        )
    )
    
    valid_to_date = forms.DateField(
        required=False,
        label="date to",
        help_text="The date configuration is valid to.",
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'aria-describedby': 'date-to-help'
            }
        )
    )
    
    valid_to_time = forms.TimeField(
        required=False,
        label="time to",
        initial="00:00:00",
        help_text="The time configuration is valid to.",
        widget=forms.widgets.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
                'aria-describedby': 'time-to-help'
            }
        )
    )
    
    version = forms.IntegerField(
        required=False,
        label="version",
        help_text="The version of the configuration.",
        initial=1,
        min_value=1,
        widget=forms.widgets.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'aria-describedby': 'version-help'
            }
        )
    )
    
    run = forms.IntegerField(
        required=False,
        label="run id",
        help_text="The run id to extract validity dates from",
        widget=forms.widgets.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'aria-describedby': 'run-help'
            }
        )
    )
    
    filename = forms.CharField(
        required=False,
        label="run file name",
        help_text="The name of run file to extract validity dates from",
        widget=forms.widgets.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'aria-describedby': 'filename-help'
            }
        )
    )
