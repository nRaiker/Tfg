# ARCHIVO DE URLS PARA LA APLICACION SUBIDA


from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^hola/', views.visualizar, name='visualizar'),
    url(r'^$', views.index, name='index'),

]