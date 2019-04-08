from django.urls import path
from django.conf.urls import url
from organisers.views import add_details, update_details
from hackathons.views import add_hackathon, get_ranking
app_name = 'organisers'

urlpatterns = [
    path('details', add_details, name='details'),
    path('updatedetails', update_details, name='updatedetails'),
    path('hackathons',add_hackathon,name='addhackathon'),
    # path('gethackathons',get_hackathons,name='gethackathons'),
    url(r'^(?P<name>[\w-]+)/$', get_ranking, name='getranking'),
]
