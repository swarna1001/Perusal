from django.shortcuts import render

# Create your views here.

def index_page(request):
    # return HttpResponse(slug)
    return render(request, 'home/index_page.html')