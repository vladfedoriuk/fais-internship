from django import forms
from core.models import Release
from django.core.exceptions import ValidationError
import datetime

class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = ['name', 'comment']
        widgets = {
            'comment': forms.widgets.Textarea(
                attrs={
                    'type': 'textarea',
                    'class': 'form-control',
                    'aria-describedby': 'comment-help',
                    'rows': 3
                }
            ),
            'name': forms.widgets.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'aria-describedby': 'name-help'
                }
            )
            
        }
        labels = {
            'name': 'name',
            'comment': 'comment'
        }
        help_texts = {
            'name': 'The name of a release.',
            'comment': 'The optional comment about a release.'
        }
        error_messages = {
            'name': {
                'invalid': 'Enter a valid name consisting of letters, numbers, underscores or hyphens.'
            }
        }
        
    def clean_name(self):
        cleaned_data = super(ReleaseForm, self).clean()
        model = self.Meta.model
        name = cleaned_data['name']
        releases = model.objects.filter(name=name)
        if len(releases) != 0:
            raise ValidationError('There is already a release with such a name in the database.')
        return cleaned_data  
            
            