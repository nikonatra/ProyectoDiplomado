#####
from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^resultado/$', views.resultado, name='resultado'),
]
