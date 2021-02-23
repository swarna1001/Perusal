from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

from accounts import views as account_views


 

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'accounts/', include('accounts.urls')),   
    path(r'', views.basic_home_view, name="basic_home"), 
    path('accounts/<slug>/', account_views.profile_view, name='profile_view'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


