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
			# return redirect('home:homepage')

			# user is directed to login page after the successful registration
			return redirect('accounts:login')


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

			return redirect('accounts:homepage')
	else:
		form = AuthenticationForm()

	return render(request, 'registration/login.html', {'form':form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)

		# temporary logout direct
		# might create a different logout view

		return redirect('basic_home/')



def homepage_view(request):
    # return HttpResponse(slug)
    return render(request, 'accounts/homepage.html')




