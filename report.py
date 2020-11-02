#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Generacion de Reportes
## Ultima Revisión: 19-11-2012 11:05 a.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 07 de Noviembre de 2012
#
# +-------------------------------------------------+#
###########################################################################

import wx
import os
import tempfile
from modeloBD import ModeloBD
from datetime import datetime

#Obtenemos de platypus las clases Paragraph, para escribir párrafos Image, para insertar imágenes y SimpleDocTemplate para definir el DocTemplate.
#Además importamos Spacer, para incluir espacios  e Image para agregar El logo en la cabecera.
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
#Importamos clase de hoja de estilo de ejemplo.
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
#Se importa el tamaño de la hoja.
from reportlab.lib.pagesizes import letter, legal, landscape, portrait
#Y los colores.
from reportlab.lib import colors

class Reportes:

    def __init__(self):
        self.BD=ModeloBD()

    def CrearVistaPreviaDoc(self, documento):
        """
        Generacion del documento PDF referente a la Vista Previa del Documento
        """

        document=self.BD.editarDocumento(documento)
        nomInst=self.BD.obtenerInstitucion(document["Institucion_inst_id"])
        nomPauta=self.BD.obtenerPauta(document["doc_id"])

        #Damos formato a la fecha de Registro para WxPython
        fechaRegistro = document['doc_fechaRegistro']
        diaRegistro = fechaRegistro.day
        mesRegistro = fechaRegistro.month
        anioRegistro = fechaRegistro.year
        fechaRegistroFormateada = wx.DateTimeFromDMY(diaRegistro,mesRegistro-1,anioRegistro)

        #Damos formato a la fecha de recepcion para WxPython
        fechaRecep = document['doc_fechaDocRecep']
        diaRecep = fechaRecep.day
        mesRecep = fechaRecep.month
        anioRecep = fechaRecep.year
        fechaRecepFormateada = wx.DateTimeFromDMY(diaRecep,mesRecep-1,anioRecep)




        ##############################################################################
        ##############################################################################


        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='Datos', alignment=TA_LEFT, fontSize=10,))

        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        datos=estiloHoja['Datos']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabeceraFicha.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen))
        imagen_logo.hAlign = 'LEFT'

        story.append(imagen_logo)
        story.append(Spacer(0,20))

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u"<b>CORRESPONDENCIA RECIBIDA DESPACHO DIRECTOR FUNDADOR</b>"
        cadena2=u"<b>FUNDAMUSICAL BOLÍVAR</b>"

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo1 = Paragraph(cadena, cabecera)
        parrafo12 = Paragraph(cadena2, cabecera)

        #Y lo incluimos en el story.

        story.append(parrafo1)
        story.append(Spacer(0,10))
        story.append(parrafo12)
        story.append(Spacer(0,80))

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        #################################################################

        fecha_rec= u"<b>FECHA DE RECEPCIÓN: </b>%s"%(str(fechaRecepFormateada)[:10])
        fecha_reg=u"<b>FECHA DE REGISTRO: </b> %s"%(str(fechaRegistroFormateada)[:10])
        oficio=u"<b>N° DE OFICIO:</b>%s"%(document['doc_numOficio'])
        tipo_doc="<b>TIPO DE DOCUMENTO: </b> %s"%(document['doc_Tipo'])
        remitente="<b>REMITENTE: </b>%s"%(document['doc_Remitente'])
        institucion=u"<b>INSTITUCIÓN: </b>%s"%(nomInst['inst_Nombre'])
        contenido="<b>CONTENIDO: </b>%s"%(document['doc_Titulo'])
        pautas="<b>PAUTAS: </b>%s"%(nomPauta['pau_recibe'])
        observaciones="<b>OBSERVACIONES: </b>%s"%(document['doc_Observaciones'])
        usuario="<b>CARGADO POR: </b>%s"%(document['usu_login'])

        parrafo2 = Paragraph(fecha_rec, datos)
        parrafo3 = Paragraph(fecha_reg, datos)
        parrafo4 = Paragraph(oficio, datos)
        parrafo5 = Paragraph(tipo_doc, datos)

        parrafo6 = Paragraph(remitente, datos)
        parrafo7 = Paragraph(institucion, datos)
        parrafo8 = Paragraph(contenido, datos)
        parrafo9 = Paragraph(pautas, datos)
        parrafo10 = Paragraph(observaciones, datos)
        parrafo13 = Paragraph(usuario, datos)

        if not datos==[]:

            #Y la asignamos al platypus story.
            story.append(parrafo2)
            story.append(Spacer(0,20))
            story.append(parrafo3)
            story.append(Spacer(0,20))
            story.append(parrafo4)
            story.append(Spacer(0,20))
            story.append(parrafo5)
            story.append(Spacer(0,20))
            story.append(parrafo6)
            story.append(Spacer(0,20))
            story.append(parrafo7)
            story.append(Spacer(0,20))
            story.append(parrafo8)
            story.append(Spacer(0,20))
            story.append(parrafo9)
            story.append(Spacer(0,20))
            story.append(parrafo10)
            story.append(Spacer(0,20))
            story.append(parrafo13)
        else:
            parrafo11=Paragraph(u'Error', cabecera)
            story.append(parrafo5)
            story.append(Spacer(0,20))

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        name = "VistaPrevia-%s-%s" % (date_str, os.getpid())
        temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir=os.environ['TEMP'],)
        temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        #doc.pagesize=landscape(letter)
        doc.build(story)

        #self.open_report(temp.name)
        self.tempFile=temp.name
        return temp.name


