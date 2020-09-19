from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from accounts import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    url(r'^$', include('home.urls')),
    url(r'signup/', v.signup_view, name="signup"),
    path('', include("django.contrib.auth.urls")),
]
 