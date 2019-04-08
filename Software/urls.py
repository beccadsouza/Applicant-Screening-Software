from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import TemplateView
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('participants/', include('participants.urls')),
    path('hackathons/', include('hackathons.urls')),
    path('profiles/', include('profiles.urls')),
    path('organisers/', include('organisers.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
