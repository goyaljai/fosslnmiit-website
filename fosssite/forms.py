from django.contrib.auth.models import User
from django import forms

from .models import UserProfile

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=['username','email','password']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname','password')