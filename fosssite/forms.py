from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=['username','email','first_name','last_name','password']

class UserProfileForm(forms.ModelForm):


	class Meta:
		model= UserProfile
		exclude= ('profileuser',)



class UserEditForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['email','first_name','last_name']
