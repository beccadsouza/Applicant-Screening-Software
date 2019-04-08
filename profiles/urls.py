from django.urls import path
from django.conf.urls import url
from .views import get_hackathons, create_profile, get_status
app_name = 'profiles'

urlpatterns = [
	url(r'^(?P<name>[\w-]+)/$', create_profile, name='createprofile'),
]
