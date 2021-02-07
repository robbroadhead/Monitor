from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from monitor.models import Sites, lkpFrequency, lkpPing, lkpResult
from . import forms
from django.views.generic import ListView

class SiteView(ListView):
	model = Sites

def HomePage(request):
	if not request.user.is_authenticated:
		return render(request,'welcome.html')
	else:
		return redirect("/sites")

def ListSites(request):
	if request.user.is_authenticated:
		sites = Sites.objects.all()
		parms={ "sites": sites}
		return render(request,'siteList.html',parms)
	else:
		return redirect("/accounts/login")

def EditSite(request,id):
	if not request.user.is_authenticated:
		return redirect("/accounts/login")

	if id != 0:
		data = Sites.objects.get(pk=id)
	else:
		data = Sites()
		
	if request.method == 'POST':
		form=forms.SiteForm(request.POST, instance = data)
		if form.is_valid():
			form.save(commit=True)
			return redirect("/sites")
	else:
		if id == 0:
			form = forms.SiteForm()
		else:
			form = forms.SiteForm(instance=data)

	parms={ "form": form, "id": id, "title": "Edit A Site"}
	return render(request,'siteEdit.html',parms)

def AddSite(request):
	if not request.user.is_authenticated:
		return redirect("/accounts/login")

	if request.method == 'POST':
		form=forms.SiteForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect("/sites")
	else:
		form = forms.SiteForm()

	parms={ "form": form, "id": id, "title": "Add A Site"}
	return render(request,'siteEdit.html',parms)

def userLogout(request):
	form = forms.UserLoginForm
	parms={ "form": form}
	logout(request)
	return render(request,'registration/login.html',parms)

def userRegister(request):
	form = forms.RegistrationForm
	parms={ "form": form}
	if request.method == 'POST':
		form=forms.RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	return render(request,'register.html',parms)

