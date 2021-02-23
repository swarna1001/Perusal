from django.conf.urls import url, include
from .import views
from django.urls import path



app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^edit_profile/$', views.edit_profile_view, name="edit_profile"),
    url(r'^my_profile/$', views.my_profile_view, name="my_profile"),
    url(r'^genres/$', views.genres_view, name="genres"),

]

