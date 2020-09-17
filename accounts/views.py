from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def index_page(request):
    # return HttpResponse(slug)
    return render(request, 'accounts/index_page.html')


def login_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect('/home')

	else:
		form = RegisterForm()
	
	return render(request, 'accounts/register.html', {'form':form})
