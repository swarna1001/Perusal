from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile

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

		#return redirect('basic_home/')
		return render(request, 'accounts/logout.html')


@login_required
def homepage_view(request):
    # return HttpResponse(slug)
    if request.method == "POST":

    	u_form = UserUpdateForm(request.POST, instance=request.user)
    	p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)


    	if u_form.is_valid() and p_form.is_valid():
    		u_form.save()
    		p_form.save()

    		messages.success(request, f'your profile has been updated!')
    		return redirect('accounts:homepage')

    	else:
    		messages.success(request, f'Fill all the fields!')

    else:

	    u_form = UserUpdateForm(instance=request.user)
	    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    	'u_form' : u_form,
    	'p_form' : p_form,
    }

    return render(request, 'accounts/homepage.html', context)


