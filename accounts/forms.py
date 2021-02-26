from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import Profile


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]



class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
	city = forms.CharField()
	state = forms.CharField()
	bio = forms.CharField()

	class Meta:
		model = Profile
		fields = ['image', "city", "state", "bio"]


"""
class Genres_choices(forms.ModelForm):
	adds_classic = forms.BooleanField()
	

	class Meta:
		model = Profile
		fields = ['adds_classic'] """




