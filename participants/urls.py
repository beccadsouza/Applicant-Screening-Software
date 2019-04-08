from django.urls import path
from django.conf.urls import url
from .views import update_details, add_details
from profiles.views import get_hackathons, create_profile, get_status
app_name = 'participants'

urlpatterns = [
	path('details', add_details, name='details'),
	path('updatedetails', update_details, name='updatedetails'),
	path('gethackathons',get_hackathons,name='gethackathons'),
	# url(r'^(?P<name>[\w-]+)/$', get_status, name='getstatus'),
	path('<parameter1>/<parameter2>',get_status, name='getstatus'),
]
