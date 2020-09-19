from django.shortcuts import render

# Create your views here.

def index_view(request):
    # return HttpResponse(slug)
    return render(request, 'home/index_page.html')


def homepage_view(request):
    # return HttpResponse(slug)
    return render(request, 'home/homepage.html')