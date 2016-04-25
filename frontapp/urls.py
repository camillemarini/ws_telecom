from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^setup$', views.setup, name='setup'),
    url(r'^materials$', views.materials, name='materials'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^registration_ok$', views.registration_ok, name='registration_ok'),
    url(r'^registration_admin$', views.registration_admin,
        name='registration_admin'),
    url(r'^vote_up_down_probicipant/(?P<probicipant_id>\d+)/$',
        views.vote_up_down_probicipant, name='vote_up_down_probicipant'),
]
