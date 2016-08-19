from django.views.generic import View
from django.utils import timezone
from .models import UserProfile
from django.shortcuts import render, get_object_or_404,render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
<<<<<<< HEAD
from django.contrib.auth import authenticate,login
from django.core.context_processors import csrf
from passlib.hash import pbkdf2_sha256
from .forms import UserForm, ProfileForm

# Create your views here.
=======
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm, UserEditForm
from .models import UserProfile, User
>>>>>>> 6c068a332a3c30eba70dad6fe128dd8ac985a811

def home(request):
	return render(request, 'fosssite/home.html')

<<<<<<< HEAD
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
=======
def login_user(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('fosssite:home')
		else:
			return render(request, 'fosssite/login.html', {'error_message': 'Invalid login'})
	return render(request,'fosssite/login.html')

>>>>>>> 6c068a332a3c30eba70dad6fe128dd8ac985a811

def UserFormView(request):
	form=UserForm(request.POST or None)
	profile_form = UserProfileForm()
	if form.is_valid():
		# not saving to database only creating object
		user=form.save(commit=False)
		profile = profile_form.save(commit=False)
		#normalized data
		user.first_name = form.data['fname']
		user.last_name = form.data['lname']
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		#not as plain data
		user.set_password(password)
		user.save() #saved to database
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			profile.profileuser = request.user
			profile.save()
			return redirect('fosssite:home')
	return render(request,'fosssite/signup.html',{'form':form})

@login_required
def profileuser(request, name):
	userprofile = get_object_or_404(UserProfile,profileuser=request.user)
	return render(request,'fosssite/profileuser.html',{'user':request.user,'userprofile':userprofile})

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

@login_required
def edit_user_profile(request, name):
	puser = get_object_or_404(UserProfile, profileuser= request.user)
	if request.method == 'POST':

		profile_form = UserProfileForm(data=request.POST, instance=puser)
		user_form = UserEditForm(data=request.POST, instance=request.user)
		if user_form.is_valid() and profile_form.is_valid():

			profile = profile_form.save(commit=False)
			profile.profileuser = request.user
			if 'avatar' in request.FILES:
				profile.avatar = request.FILES['avatar']
				if profile.avatar.size > 1048576:
					errors= 'Max File Size is 1 MB'
					return render(request,'fosssite/edituser.html',{'profile_form':profile_form,'user_form':user_form,'errors':errors})
			profile_form.save()
			user_form.save()
			return redirect('fosssite:profileuser',name=request.user)
	else:
		profile_form = UserProfileForm(instance=puser)
		user_form = UserEditForm(instance=request.user)
	return  render(request,'fosssite/edituser.html',{'profile_form':profile_form, 'user_form':user_form})

<<<<<<< HEAD
def invalid_login(request):
	return render_to_response('fosssite/invalid_login.html')

def view_profile(request):
    url = request.user.profile.url
=======
@login_required
def changepassword(request, name):
	if request.method=='POST':
		user = User.objects.get(username=request.user)
		current_password = request.POST.get('current_password')
		if user.check_password(current_password):
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')
			if password1 == password2 and len(password1) !=0:
				user.set_password(password1)
				user.save()
				user = auth.authenticate(username=user.username,password=password1)
				if user is not None:
					auth.login(request, user)
					return redirect('fosssite:profileuser', name=request.user)
			else:
				error = 'New Password Must Match or valid!'
				return render(request, 'fosssite/changepassword.html',{'error':error})
		else:
			error = 'Current Password not Matched!'
			return render(request,'fosssite/changepassword.html',{'error':error})
	return render(request,'fosssite/changepassword.html')


def events(request):
	if request.user.is_authenticated():
		return render(request,'fosssite/working.html',{})
	return render(request, 'fosssite/events.html')


def contributions(request):
	if request.user.is_authenticated():
		return render(request,'fosssite/working.html',{})
	return render(request, 'fosssite/contributions.html')


def blog(request):
	if request.user.is_authenticated():
		return render(request,'fosssite/working.html',{})
	return render(request, 'fosssite/blog.html')
>>>>>>> 6c068a332a3c30eba70dad6fe128dd8ac985a811
