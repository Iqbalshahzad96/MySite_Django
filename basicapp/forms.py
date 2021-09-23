from django import forms
from django.core import validators

#Validater check Name Starts With 'Z'
def check_for_Z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name Needs to Start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_Z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,
                                widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)]) #used django.core validator

#Writing your own validator
"""     def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher """