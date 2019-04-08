from django import forms
from . import models

class CreateOrganiser(forms.ModelForm):
    class Meta:
        model = models.Organiser
        fields = ['name', 'website', 'poc', 'contact']

