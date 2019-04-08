from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from organisers.models import Organiser
from hackathons.models import Hackathon
from hackathons.views import get_ranking
from django.core import serializers
from ast import literal_eval
from django.http import JsonResponse,HttpResponse
from profiles.models import Profile
from . import forms
from accounts.models import CustomUser

@login_required()
def add_details(request):
	if not request.user.is_organiser:
		return redirect('home')
	if request.method == 'POST':
		form = forms.CreateOrganiser(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			request.user.details_set = True
			request.user.save()
			instance.save()
			return render(request,'organiser/home.html')
	else:
		form = forms.CreateOrganiser()
	return render(request, 'organiser/details.html', {'form': form})

@login_required()
def update_details(request):
	x = {}
	qs = Organiser.objects.filter(user__email=request.user.email)
	if len(qs) != 0:
		x = literal_eval(serializers.serialize('json',qs))[0]['fields']
		print(x)
	return JsonResponse(x)

@login_required()
def set_status(request,parameter1,parameter2,parameter3):
	x = Profile.objects.filter(hackathon__name=parameter2).get(participant__user__username=parameter1)
	x.status_set = True


	"""
	USER AND HACKATHON INFORMATION STORED IN THIS VARIABLE
	
	"""

	email = CustomUser.objects.get(username=parameter1)
	hackathon = Hackathon.objects.get(name=parameter2)



	if parameter3 == 'accept':
		x.selected = True


		"""
		SEND ACCEPTANCE MAIL, using email and hackathon variables
		"""


	else:
		x.selected = False

		"""
		SEND REJECTION MAIL, using email and hackathon variables
		"""



	x.save()
	return get_ranking(request,Hackathon.objects.get(name=parameter2).name_id)
