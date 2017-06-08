#!/usr/bin/python2.7

import os
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject, createStringObject


def InformacionPDF(nombre):

    pdf_toread = PdfFileReader(open(nombre, "rb"))
    pdf_info = pdf_toread.getDocumentInfo()
    
    metadatos=[]

    for p in pdf_info:
        metadatos = metadatos + [ p[1:] + ": " + pdf_info[p]]

    return metadatos

def BorrarMetadatos(nombre,carpeta,noborrar):

    NombreSalida = carpeta + "aux.pdf"
    salida=PdfFileWriter()

    infoDict = salida._info.getObject()



    entrada = PdfFileReader(open(nombre, "rb"))
    pdf_info = entrada.getDocumentInfo()


    for md in noborrar:

            infoDict.update({
                NameObject('/'+md[:-1]): createStringObject(pdf_info['/'+md[:-1]]),
            })

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