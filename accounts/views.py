from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)

		if form.is_valid():
			user = form.save()

			# log the user in
			login(request, user)
			# user is directed to his homepage, after successful login
			return redirect('home:homepage')
	else:
		form = RegisterForm()
	
	return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():

			#log in the user
			user = form.get_user()
			login(request, user)

			return redirect('home:homepage')
	else:
		form = AuthenticationForm()

	return render(request, 'registration/login.html', {'form':form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)

		return redirect('basic_home/')

