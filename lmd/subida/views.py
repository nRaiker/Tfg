# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from django.conf import settings

from subida.forms import UploadForm
from subida.models import Document


def index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
            print type(newdoc)
            newdoc.save(form)
            return redirect("index")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'subida.html', {'form': form})

def visualizar(request):
    
    archivos=Document.objects.all()
    IP = request.META.get('REMOTE_ADDR')
    print IP  
    print settings.MEDIA_ROOT + str(archivos[0])
    return render(request,'metadata.html',{'metadata':archivos})
