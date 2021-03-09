from django.conf.urls import url, include
from .import views
from django.urls import path

app_name = 'feed'

urlpatterns = [

			url(r'^post/new/$', views.create_post, name='post-create'),
			




]