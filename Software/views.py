from django.shortcuts import render
from participants.forms import CreateParticipant
from organisers.forms import CreateOrganiser
from hackathons.models import Hackathon
from profiles.models import Profile


def home(request):
	if request.user.is_authenticated:
		if request.user.is_organiser:
			if request.user.details_set:

				qs = Hackathon.objects.filter(organiser__user__email=request.user.email)

				return render(request, 'organiser/home.html',{'hackathons':qs})
			else:
				form = CreateOrganiser()
				return render(request, 'organiser/details.html', {'form': form, "details_set": False})
		else:
			if request.user.details_set:

				l = Profile.objects.filter(participant__user=request.user)
				qs = [x.hackathon for x in l]
				return render(request, 'participant/home.html',{'hackathons':qs})
			else:
				form = CreateParticipant()
				return render(request, 'participant/details.html', {'form': form, 'details_set':False})
	else:
		return render(request, 'home.html')
