from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

from .models import UserProfile

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
<<<<<<< HEAD
		fields=['username','email','password']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname','password')
=======
		fields=['username','email','first_name','last_name','password']

class UserProfileForm(forms.ModelForm):


	class Meta:
		model= UserProfile
		exclude= ('profileuser',)



class UserEditForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['email','first_name','last_name']
>>>>>>> 6c068a332a3c30eba70dad6fe128dd8ac985a811
