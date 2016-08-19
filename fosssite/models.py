from django.contrib.auth.models import User
from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

from django.utils import timezone
from passlib.hash import pbkdf2_sha256

# Create your models here.
class UserProfile(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	username=models.CharField(max_length=200)
	email=models.ForeignKey('auth.User')
	password=models.CharField(max_length=200)

	User.profile = property(lambda u: UserProfile.objects.get_or_create(email=u)[0])

	def verify_password(self,raw_password):
		return pbkdf2_sha256.verify(raw_password,self.password)
=======
#from django.utils import timezone
#from django.core.exceptions import ValidationError

class UserProfile(models.Model):
	profileuser = models.OneToOneField(User)
	handle = models.CharField(max_length=128, blank=True)
	avatar = models.ImageField(upload_to='profile_images', blank=True)
	about_me = models.TextField(max_length=100,blank=True)
	twitterurl = models.URLField(blank=True)
	facebookurl = models.URLField(blank=True)
	lnkdnurl = models.URLField(blank=True)
	githuburl = models.URLField(blank=True)
	example = models.URLField(blank=True)

	def __str__(self):
		return self.profileuser.username
>>>>>>> 6c068a332a3c30eba70dad6fe128dd8ac985a811
