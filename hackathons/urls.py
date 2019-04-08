from django.urls import path
from django.conf.urls import url
from organisers.views import set_status
app_name = 'hackathons'

urlpatterns = [
    path('<parameter1>/<parameter2>/<parameter3>',set_status, name='setstatus'),
]
