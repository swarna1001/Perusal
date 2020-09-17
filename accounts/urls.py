from django.conf.urls import url, include
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index_page, name="index"),
]