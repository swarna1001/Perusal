from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from accounts import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    url(r'', v.login_view, name="login"),
]
 