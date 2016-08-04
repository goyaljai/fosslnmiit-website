from django.views.generic import View
from django.utils import timezone
from .models import UserProfile
from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.core.context_processors import csrf
from passlib.hash import pbkdf2_sha256
from .forms import UserForm, ProfileForm

# Create your views here.

def home(request):
	return render(request, 'fosssite/home.html')

def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('fosssite/login.html',c)

def UserFormView(request):
	form_class=UserForm
	template_name='fosssite/signup.html'

	if request.method=='GET':
		form=form_class(None)
		return render(request,template_name,{'form':form})


		#submission
	if request.method=='POST':
		form=form_class(request.POST)

		if form.is_valid():
			# not saving to database only creating object
			user=form.save(commit=False)
			#normalized data
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			#not as plain data
			user.set_password(password)
			user.save() #saved to database

			user=auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return HttpResponseRedirect('/')#url in brackets

			return render(request,template_name,{'form':form})

def auth_view(request):
	firstname=request.POST.get('firstname','')
	username=request.POST.get('username', '')
	password=request.POST.get('password', '')
	user=auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/profileuser')#url in brackets
	else:
		return HttpResponseRedirect('/invalid')

def post_edit(request):
	form_class=ProfileForm
	template_name='fosssite/edituser.html'

	if request.method=='GET':
		form=form_class(None)
		return render(request,template_name,{'form':form})

	if request.method == "POST":
		userprofile = get_object_or_404(UserProfile)
		form = form_class(request.POST, instance=userprofile)

		if form.is_valid():
			userprofile = form.save(commit=False)
			userprofile.username = request.username
			userprofile.save()
			return redirect('profileuser')
		else:
			form = ProfileForm(instance=userprofile)
		return render(request, 'fosssite/profileuser.html', {'form': form})

def profileuser(request):
	#url = request.user.profile.url
	return render_to_response('fosssite/profileuser.html',{'username':request.user.username})

def logout(request):
	auth.logout(request)
	pass

def edit_user_profile(request):
	pass

def invalid_login(request):
	return render_to_response('fosssite/invalid_login.html')

def view_profile(request):
    url = request.user.profile.url