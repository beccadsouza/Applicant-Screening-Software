from django.db import models
from accounts.models import CustomUser


def user_directory_path(instance, request):
	# file will be uploaded to MEDIA_ROOT/resume/user_username
	print(instance.user.username)
	return 'resume/{0}.txt'.format(instance.user.username)


class Participant(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
	first_name = models.CharField(max_length=30,default=None)
	last_name = models.CharField(max_length=30,default=None)
	institution = models.CharField(max_length=150,default=None)
	locality = models.CharField(max_length=100,default=None)
	github_username = models.CharField(max_length=30,default=None)
	linkedin_url = models.URLField(default=None)
	resume = models.FileField(upload_to=user_directory_path)

	def __str__(self):
		return self.first_name + " " + self.last_name

