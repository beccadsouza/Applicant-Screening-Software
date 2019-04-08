from django import forms
from . import models

class CreateHackathon(forms.ModelForm):
    class Meta:
        model = models.Hackathon
        fields = ['name', 'location', 'time', 'date', 'desc','poster',]
