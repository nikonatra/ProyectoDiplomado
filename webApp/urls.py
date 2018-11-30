#####
from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^resultado/$', views.resultado, name='resultado'),
     url(r'^login/$', views.login, name='login'),
     url(r'^index/$', views.index, name='index'),
     url(r'^analistas/$', views.fanalistas, name='fanalistas'),
     url(r'^entidades/$', views.fentidades, name='fentidades'),
]
