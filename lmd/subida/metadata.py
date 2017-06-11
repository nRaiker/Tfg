#!/usr/bin/python2.7

import os
import sys
from subprocess import Popen, PIPE

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject, createStringObject


def ExtraerMetadatos(nombre):

    metadatos=None 
    
    if nombre[-4:] == '.pdf':
        metadatos = InformacionPDF(nombre)

    else:
        metadatos = InformacionImagen(nombre)

    return metadatos


def BorrarMetadatos(nombre,carpeta,noborrar):

    if nombre[-4:]=='.pdf':
        BorrarMetadatosPDF(nombre,carpeta,noborrar)
    else:
        BorrarImagen(nombre,carpeta,noborrar)


#Extraccion y borrado de metadatos de documentos pdf 



def InformacionImagen(nombre):
    info_imagen = Popen(['exiftool', nombre],stdout=PIPE)
    info_imagen = info_imagen.communicate()[0]
    info_imagen = info_imagen.split("\n")

    md_aux = []
    metadatos = []

    for x in info_imagen:
        aux = x.split(':')
        aux[0] = aux[0].strip().replace(" ","")
        md_aux = md_aux + [aux[0]]

        if len(aux)>1:
            metadatos = metadatos + [{'tag':aux[0] 
                ,'meta':aux[0] + ": " + aux[1]}]





    return metadatos

def BorrarImagen(nombre,carpeta,noborrar):

    md_origen = Popen(['exiftool', nombre],stdout=PIPE)
    md_origen = md_origen.communicate()[0]
    md_origen = md_origen.split("\n")

    md_aux=[]

    for p in md_origen:
        aux = p.split(':')
        aux[0] = aux[0].strip().replace(" ","")
        md_aux = md_aux + [aux[0]]


    salida = Popen(['exiftool', '-all=' ,nombre],stdout=PIPE)
    salida = salida.communicate()

    for tag in noborrar:
        if tag in md_aux:
            salida = Popen(['exiftool', '-' + tag + '=" "' ,nombre],stdout=PIPE)
            salida = salida.communicate()



def InformacionPDF(nombre):

    pdf_toread = PdfFileReader(open(nombre, "rb"))
    pdf_info = pdf_toread.getDocumentInfo()
    
    metadatos=[]

    for p in pdf_info:
        metadatos = metadatos + [{'tag':p[1:].replace(" ","") 
            ,'meta':p[1:] + ": " + pdf_info[p]}]

    return metadatos

def BorrarMetadatosPDF(nombre,carpeta,noborrar):

    NombreSalida = carpeta + "aux.pdf"
    salida=PdfFileWriter()

    infoDict = salida._info.getObject()



    entrada = PdfFileReader(open(nombre, "rb"))
    pdf_info = entrada.getDocumentInfo()

    for md in noborrar:

            infoDict.update({
                NameObject('/'+md): createStringObject(pdf_info['/'+md]),})

    infoDict.update({
        NameObject('/Producer'): createStringObject(u''),

    })

    

    for page in range(entrada.getNumPages()):
        salida.addPage(entrada.getPage(page))


    outputStream = file(NombreSalida, 'wb')
    salida.write(outputStream)
    outputStream.close()


    os.remove(nombre)
    os.rename(NombreSalida,nombre)