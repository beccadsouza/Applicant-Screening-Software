from django import forms
from . import models

class CreateParticipant(forms.ModelForm):
    class Meta:
        model = models.Participant
        fields = ['first_name', 'last_name', 'github_username', 'linkedin_url', 'resume', 'institution', 'locality']

