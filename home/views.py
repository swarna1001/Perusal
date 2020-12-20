from django.shortcuts import render

# Create your views here.


def homepage_view(request):
    # return HttpResponse(slug)
    return render(request, 'home/homepage.html')