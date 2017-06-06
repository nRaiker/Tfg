#!/usr/bin/python2.7

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import NameObject, createStringObject


def InformacionPDF(nombre):

    pdf_toread = PdfFileReader(open(nombre, "rb"))
    pdf_info = pdf_toread.getDocumentInfo()
    
    metadatos=[]

    for p in pdf_info:
        metadatos=metadatos+[ p[1:] + ": " +pdf_info[p]]

    return metadatos

def BorrarMetadatos(nombre):

    NombreSalida=nombre
    salida=PdfFileWriter()

    infoDict = salida._info.getObject()

    infoDict.update({
        NameObject('/Producer'): createStringObject(u''),

    })

    entrada=PdfFileReader(open(sys.argv[1], "rb"))

    for page in range(entrada.getNumPages()):
        salida.addPage(entrada.getPage(page))


    outputStream = file(NombreSalida, 'wb')
    salida.write(outputStream)
    outputStream.close()