# ARCHIVO DE URLS PARA LA APLICACION SUBIDA


from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^visualizar/', views.visualizar, name='visualizar'),
	url(r'^borrado/', views.borrado, name='borrado'),
	url(r'^descarga/', views.descarga, name='descarga'),
    url(r'^$', views.principal, name='principal'),

]