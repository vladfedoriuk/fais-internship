from django import forms
from django.core.exceptions import ValidationError
import datetime
from datetime import time

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
        # initial="00:00:00",
        help_text="The time configuration is valid from. If not provided, will be set to 00:00",
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
        # initial="00:00:00",
        help_text="The time configuration is valid to. If not provided, will be set to 23:59",
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
        min_value=0,
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
    
    SEARCH_CHOICES = (
        ('dates', 'dates'),
        ('runs', 'runs')
    )
    
    search_option = forms.ChoiceField(
        required=True,
        choices=SEARCH_CHOICES,
        widget=forms.widgets.RadioSelect(
            attrs={
                'type': 'radio',
            }
        )
    )
    
    def clean(self):
        cleaned_data = super(ExtractForm, self).clean()
        
        valid_from_date = cleaned_data.get('valid_from_date')
        valid_from_time = cleaned_data.get('valid_from_time')
        valid_to_date = cleaned_data.get('valid_to_date')
        valid_to_time = cleaned_data.get('valid_to_time')
        
        search_dates = cleaned_data.get('search_option') == 'dates'
        search_runs = not search_dates
        
        if search_dates and valid_from_time and not valid_from_date:
            raise ValidationError(
                'The date the configuration is valid from is required if the relevant time is specified.'
            )
            
        if search_dates and valid_to_time and not valid_to_date:
            raise ValidationError(
                'The date the configuration is valid to is required if the relevant time is specified.'
            )
            
        if search_dates and (
            (valid_from_date and not valid_to_date) or (valid_to_date and not valid_from_date)):
            raise ValidationError(
                'If any of the validity dates is specified, then another one must be given too.'
            )
            
        if search_dates and valid_from_date and valid_to_date:
            if valid_from_time:
                self.cleaned_data['valid_from'] = datetime.datetime.combine(
                    valid_from_date, valid_from_time)
            else:
                self.cleaned_data['valid_from'] = datetime.datetime.combine(
                    valid_from_date, time(hour=0, minute=0, second=0))
            
            if valid_to_time:
                self.cleaned_data['valid_to'] = datetime.datetime.combine(
                    valid_to_date, valid_to_time)
            else:
                self.cleaned_data['valid_to'] = datetime.datetime.combine(
                    valid_to_date, time(hour=23, minute=59, second=59))
                
            return self.cleaned_data
            
        elif search_runs: 
            run = cleaned_data.get('run')
            filename = cleaned_data.get('filename')
            if not run and not filename:
                raise ValidationError(
                    'Either run id or filename must be specified if the validity dates are omitted.'
                )
                
            return self.cleaned_data
        
        raise ValidationError('No valid search options were provided.')