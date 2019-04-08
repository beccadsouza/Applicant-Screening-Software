from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hackathons.models import Hackathon
from django.core import serializers
from ast import literal_eval
from django.http import JsonResponse, HttpResponse
from . import forms
from profiles.models import Profile
from accounts.models import CustomUser

@login_required()
def add_hackathon(request):
	if not request.user.is_organiser:
		return redirect('home')
	if request.method == 'POST':
		form = forms.CreateHackathon(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.name_id = instance.name.replace(" ","").lower()
			instance.organiser = request.user.organiser
			instance.save()
			qs = Hackathon.objects.filter(organiser__user__email=request.user.email)
			return render(request, 'organiser/home.html', {'hackathons': qs})
	else:
		form = forms.CreateHackathon()
	return render(request, 'organiser/hackathon.html', {'form':form})

# @login_required()
# def get_hackathons(request):
# 	# qs = Hackathon.objects.filter(organiser__user__email='anna@gmail.com')
# 	x = {}
# 	qs = Hackathon.objects.filter(organiser__user__email=request.user.email)
# 	if len(qs) != 0:
# 		x = literal_eval(serializers.serialize('json',qs))
# 	return JsonResponse(x, safe=False)

@login_required()
def get_ranking(request, name):
	hack_name = Hackathon.objects.get(name_id=name)
	x = Profile.objects.filter(hackathon__name_id=name).filter(status_set=False)
	z = [y.participant.user.username for y in x]
	print(z)
	"""
	INPUT TO RANKING MODEL  : z = ['becca','surabhi','rohit']
	
	OUTPUT OF RANKING MODEL : z = ['surabhi','becca','rohit']
	"""
	temp = []
	for un in z:
		_ = Profile.objects.filter(hackathon__name_id=name).filter(participant__user__username=un)
		temp += _
	return render(request,'organiser/ranking.html',{'profiles':temp,'hackathon':hack_name.name})
