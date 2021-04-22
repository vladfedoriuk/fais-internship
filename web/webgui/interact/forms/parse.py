from django import forms
from django.core.exceptions import ValidationError
import datetime
from core.models import Release

class ParseForm(forms.Form):
    
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
        # initial="00:00:00",
        help_text="The time configuration is valid to.",
        widget=forms.widgets.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control',
                'aria-describedby': 'time-to-help'
            }
        )
    )
    
    run_from = forms.IntegerField(
        required=False,
        label="run-from id",
        help_text="The id of a run from which configuration is valid",
        min_value=0,
        widget=forms.widgets.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'aria-describedby': 'run-from-help'
            }
        )
    )
    
    run_to = forms.IntegerField(
        required=False,
        label="run-to id",
        help_text="The id of a run up to which configuration is valid",
        min_value=0,
        widget=forms.widgets.NumberInput(
            attrs={
                'type': 'number',
                'class': 'form-control',
                'aria-describedby': 'run-to-help'
            }
        )
    )
    
    filename_from = forms.CharField(
        required=False,
        label="run-from file name",
        help_text="The name of a run file from which configuration is valid",
        max_length=255,
        widget=forms.widgets.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'aria-describedby': 'filename-from-help'
            }
        )
    )
    
    filename_to = forms.CharField(
        required=False,
        label="run-to file name",
        help_text="The name of a run file up to which configuration is valid",
        max_length=255,
        widget=forms.widgets.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control',
                'aria-describedby': 'filename-to-help'
            }
        )
    )
    
    remarks = forms.CharField(
        required=False,
        label="Optional remarks about the configuration.",
        max_length=255,
        widget=forms.widgets.Textarea(
            attrs={
                'type': 'textarea',
                'class': 'form-control',
                'aria-describedby': 'remarks-help',
                'rows': 3
            }
        )
    )
    
    version = forms.IntegerField(
        required=True,
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
    
    configuration = forms.FileField(
        required=True,
        label='configuration file',
        help_text='The file containing configurations.',
        widget=forms.widgets.FileInput(
            attrs={
                'type': 'file',
                'class': 'form-control',
                'aria-describedby': 'configuration-help'
            }
        )
    )
    
    release = forms.ModelChoiceField(
        required=True,
        label='release',
        queryset=Release.objects.all(),
        to_field_name='name',
        help_text="The release the configuration will be assigned to.",
        widget=forms.widgets.Select(
            attrs={
                'type': 'select',
                'class': 'form-control',
                'aria-describedby': 'release-help'
            }
        )
    )
    
    
    def clean(self):
        cleaned_data = super(ParseForm, self).clean()
        
        valid_from_date = cleaned_data.get('valid_from_date')
        valid_from_time = cleaned_data.get('valid_from_time')
        valid_to_date = cleaned_data.get('valid_to_date')
        valid_to_time = cleaned_data.get('valid_to_time')
        
        if valid_from_time and not valid_from_date:
            raise ValidationError(
                'The date the configuration is valid from is required if the relevant time is specified.'
            )
            
        if valid_to_time and not valid_to_date:
            raise ValidationError(
                'The date the configuration is valid to is required if the relevant time is specified.'
            )
            
        if (valid_from_date and not valid_to_date) or (valid_to_date and not valid_from_date):
            raise ValidationError(
                'If any of the validity dates are specified, then another one must be given too.'
            )
            
        if valid_from_date and valid_to_date:
            if valid_from_time:
                self.cleaned_data['valid_from'] = datetime.datetime.combine(
                    valid_from_date, valid_from_time)
            else:
                self.cleaned_data['valid_from'] = valid_from_date
            
            if valid_to_time:
                self.cleaned_data['valid_to'] = datetime.datetime.combine(
                    valid_to_date, valid_to_time)
            else:
                self.cleaned_data['valid_to'] = valid_to_date
                
            return self.cleaned_data
  
        run_from = cleaned_data.get('run_from')
        run_to = cleaned_data.get('run_to')
        filename_from = cleaned_data.get('filename_from')
        filename_to = cleaned_data.get('filename_to')
        
        if ( not run_from and run_to ) or ( run_from and not run_to ):
            raise ValidationError(
                'If any of the run-id\'s are specified, another one must be provided too.'
            )
        if ( not filename_from and filename_to ) or ( filename_from and not filename_to ):
            raise ValidationError(
                'If any of the run filenames are specified, another one must be provided too.'
            )
        if ( run_from and run_to ) or ( filename_from and filename_to ):
            return self.cleaned_data
        
        raise ValidationError(
            'Either run id\'s, filenames or validation dates must be specified'
        )
    