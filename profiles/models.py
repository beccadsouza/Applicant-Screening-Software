from django.db import models
from participants.models import Participant
from hackathons.models import Hackathon
# Create your models here.

class Profile(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
	hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
	selected = models.BooleanField(default=False)
	status_set = models.BooleanField(default=False)

	def __str__(self):
		return self.participant.user.username + " has signed up for " + self.hackathon.name
