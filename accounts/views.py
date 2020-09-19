from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def signup_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect('/home')

	else:
		form = RegisterForm()
	
	return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
	return render(request, 'accounts/login_page.html')
