from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from participants.models import Participant
from django.core import serializers
from ast import literal_eval
from . import forms

@login_required()
def add_details(request):
	if request.user.is_organiser:
		return redirect('home')
	if request.method == 'POST':
		form = forms.CreateParticipant(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			request.user.details_set = True
			request.user.save()
			instance.save()
			return render(request,'participant/home.html')
	else:
		form = forms.CreateParticipant()
	return render(request, 'participant/details.html', {'form': form})

@login_required()
def update_details(request):
	x = {}
	qs = Participant.objects.filter(user__email=request.user.email)
	if len(qs) != 0:
		x = literal_eval(serializers.serialize('json',qs))[0]['fields']
		print(x)
	return JsonResponse(x)

