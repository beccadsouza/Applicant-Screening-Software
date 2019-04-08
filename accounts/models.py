from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	is_organiser = models.BooleanField(default=False)
	details_set = models.BooleanField(default=False)
	REQUIRED_FIELDS = ['email', 'is_organiser']

	def __str__(self):
		return self.email
