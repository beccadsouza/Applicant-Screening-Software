from django.db import models
from accounts.models import CustomUser



class Organiser(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=100,default=None)
	poc = models.CharField(max_length=100,default=None)
	contact = models.CharField(max_length=20,default=None)
	website = models.URLField(default=None)

	def __str__(self):
		return self.name

