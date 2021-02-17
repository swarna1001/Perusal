from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import Profile


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	city = forms.CharField()
	state = forms.CharField()


	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2", "city", "state"]



class UserUpdateForm(forms.ModelForm):

	email = forms.EmailField()
	city = forms.CharField()
	state = forms.CharField()


	class Meta:
		model = User
		fields = ["username", "email", "city", "state"]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

