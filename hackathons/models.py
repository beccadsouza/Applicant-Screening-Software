from django.db import models
from organisers.models import Organiser


class Hackathon(models.Model):
	name = models.CharField(max_length=100,default=None,primary_key=True)
	name_id = models.CharField(max_length=20,default=None)
	location = models.CharField(max_length=200, default=None)
	time = models.TimeField()
	date = models.DateField()
	desc = models.TextField(max_length=500,default=None)
	poster = models.FileField(upload_to='poster/')
	organiser = models.ForeignKey(Organiser,on_delete=models.CASCADE)

	def __str__(self):
		return self.name + " by "+ self.organiser.name
