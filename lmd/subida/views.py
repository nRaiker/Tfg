# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.conf import settings

from subida.forms import UploadForm
from subida.models import Document

import os


def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():

            IP = request.META.get('REMOTE_ADDR')
            entrada=Document.objects.filter(propietario=IP)
            if entrada:
                for i in entrada:
                    filepath=settings.MEDIA_ROOT + str(i)
                    print filepath
                    if(os.path.isfile(filepath)):
                        print "Borrando"
                        os.remove(filepath)
                    i.delete()

            newdoc = Document(propietario = IP,docfile = request.FILES['docfile'])
            newdoc.save(form)
            return redirect("index")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'subida.html', {'form': form})

def visualizar(request):
    
    IP = request.META.get('REMOTE_ADDR')
    archivos=Document.objects.filter(propietario=IP)
    return render(request,'metadata.html',{'metadata':archivos})
