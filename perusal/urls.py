from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
#from accounts import views as v

from .import views

 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),

    # new changes (recent version)

    #url(r'', include('home.urls')),
    url(r'^$', views.basic_home_view, name="basic_home"),
    #url(r'accounts/', include('accounts.urls')),


    # old version
    #url(r'accounts/', include('accounts.urls')),
    #url(r'', include('home.urls')),
    #url(r'signup/', v.signup_view, name="signup"),
    #path('', include("django.contrib.auth.urls")),

]
 