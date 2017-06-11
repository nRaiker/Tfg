# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import os
import sys

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from subida.forms import UploadForm
from subida.models import Document
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str


import metadata



def principal(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():

            IP = request.META.get('REMOTE_ADDR')
            entrada = Document.objects.filter(propietario=IP)
            if entrada:
                for i in entrada:
                    filepath = settings.MEDIA_ROOT + str(i)
                    if(os.path.isfile(filepath)):
                        os.remove(filepath)
                    i.delete()

            newdoc = Document(propietario = IP,docfile = request.FILES['docfile'])
            newdoc.save(form)
            return redirect("principal")
    else:
        form = UploadForm()
        return render(request, 'subida.html', {'form': form})

def visualizar(request):
    

    IP = request.META.get('REMOTE_ADDR')
    archivos = Document.objects.filter(propietario=IP)
    for i in archivos:
        filepath = settings.MEDIA_ROOT+str(i)
        fp = str(i)

    metadatos = metadata.ExtraerMetadatos(filepath)


    return HttpResponse(render(request,'metadata.html',{'metadata':metadatos,'documento':filepath}))


def borrado(request):


    if request.method == 'POST':

        IP = request.META.get('REMOTE_ADDR')

        archivos=Document.objects.filter(propietario=IP)
        for i in archivos:

            filepath = settings.MEDIA_ROOT+str(i)

        carpeta = settings.MEDIA_ROOT + "documents/"


        noborrar = []

        for i in request.POST.items():
            noborrar = noborrar + [i[0]]

        if 'csrfmiddlewaretoken' in noborrar:
            noborrar.remove('csrfmiddlewaretoken')

        metadata.BorrarMetadatos(filepath,carpeta,noborrar)
        metadatos = metadata.ExtraerMetadatos(filepath)

        return HttpResponse(render(request,'borrado.html',{'metadata':metadatos,'documento':filepath}))

    else:
        return redirect("principal")

def descarga(request):


    IP = request.META.get('REMOTE_ADDR')
    archivos = Document.objects.filter(propietario=IP)

    for i in archivos:

        filepath = settings.MEDIA_ROOT+str(i)
        fp=str(i)

    nombre = "limpio-" + fp[10:]

    wrapper = FileWrapper(file(filepath))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(nombre)
    response['Content-Length'] = os.path.getsize(filepath)

    return response