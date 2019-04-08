from django.shortcuts import render, redirect
from hackathons.models import Hackathon
from .models import Profile
# Create your views here.

def create_profile(request, name):
	if request.user.is_organiser:
		return redirect('home')
	profile = Profile()
	profile.participant = request.user.participant
	profile.hackathon = Hackathon.objects.get(name_id=name)
	profile.selected = False
	profile.status_set = False
	profile.save()
	return get_hackathons(request)


def get_hackathons(request):
	existing_hackathons = list(Hackathon.objects.all())
	signedup_hackathons = Profile.objects.filter(participant__user=request.user)
	[existing_hackathons.remove(x.hackathon) for x in signedup_hackathons]
	hackathons = existing_hackathons
	return render(request, 'participant/upcominghackathons.html',{'hackathons':hackathons})

def get_status(request, parameter1,parameter2):
	x = Profile.objects.filter(hackathon__name_id=parameter1)
	y = x.get(participant__user__username=parameter2)
	print(y)
	return render(request,'participant/status.html',{"profile":y})
