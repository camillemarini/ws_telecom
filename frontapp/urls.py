from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^setup$', views.setup, name='setup'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^registration_ok$', views.registration_ok, name='registration_ok'),
]
