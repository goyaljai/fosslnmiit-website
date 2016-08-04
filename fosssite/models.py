from django.db import models
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
