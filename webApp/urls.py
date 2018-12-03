#####
from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^login/$', views.login, name='login'),
     url(r'^index/$', views.index, name='index'),
     url(r'^analistas/$', views.fanalistas, name='fanalistas'),
     url(r'^entidades/$', views.fentidades, name='fentidades'),
     url(r'^comercializadoras/$', views.fcomercializadoras, name='fcomercializadoras'),
     url(r'^provedores/$', views.fprovedores, name='fprovedores'),
     url(r'^modelo/$', views.fmodelo, name='fmodelo'),
     url(r'^acerca/$', views.facerca, name='facerca')
]
