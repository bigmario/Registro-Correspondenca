#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Manejo General del Sistema (CONTROLADOR)
## Ultima Revisión: 16-01-2013 3:55 p.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 16 de Enero de 2013
#
# +-------------------------------------------------+#
###########################################################################

import wx
from wx.lib.wordwrap import wordwrap
import wx.lib.dialogs
import sys
import os
import hashlib
import MySQLdb
from modeloBD import ModeloBD
from report import Reportes
from fundamusical_vista import (FramePrincipal, FrameInicioSesion, FrameEliminarUsuario, FrameAgregarUsuario, FrameBusqueda,
                                                 FrameVPImpresion, panelPCarga, panelPEdicion, panelBienvenida, WizardConfigInicial, FrameRecuerdaPass, FrameCambioContrasena)
from fundamusical_vista import (ID_AGREGAR_USUARIO, ID_ELIMINAR_USUARIO, ID_CARGAR, ID_BUSCAR)
from wx.lib.mixins.listctrl import CheckListCtrlMixin
import logging
import traceback
import string

if wx.Platform == '__WXMSW__':
    from wx.lib.pdfwin import PDFWindow
    import win32api
else:
    mensajeWin=wx.MessageDialog(self,"Esta Aplicacion es compatible con MS Windows.\n\n","Error de Compatibilidad", wx.OK|wx.ICON_INFORMATION)
    mensajeWin.ShowModal()

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

bitmapDir = os.path.relpath(os.path.join(dirName, 'bitmaps'))
iconDir=os.path.relpath(os.path.join(dirName, 'icon'))
licenceDir=os.path.relpath(os.path.join(dirName, 'license'))
tempDir=os.path.relpath(os.path.join(dirName, 'temp'))
sys.path.append(os.path.split(dirName)[0])
padding = 5


class WizardInicio(WizardConfigInicial):

    def WizardConfigInicialOnWizardCancel( self, event ):
        pass

    def WizardConfigInicialOnWizardPageChanged(self, event):
        """
        Se Sobreescriben las etiquetas de los botones 'Next', 'Previous' y 'Finish'
        """
        cancel_btn = self.FindWindowById(wx.ID_CANCEL)
        cancel_btn.SetLabel("Cancelar")
        prev_btn = self.FindWindowById(wx.ID_BACKWARD)
        prev_btn.SetLabel("Anterior")
        next_btn = self.FindWindowById(wx.ID_FORWARD)
        if next_btn.GetLabel()=="&Finish":
            next_btn.SetLabel("Finalizar")
        else:
            next_btn.SetLabel("Siguiente")

    def WizardConfigInicialOnWizardPageChanging(self, event):
        """
        Validaciones al momento de cambiar de Pagina
        """

        page=event.GetPage()

        try:
            #si estamos en la pagina de datos de Usuario administrador
            if page==self.wizPageUsuario and event.GetDirection():
                self.nomAdmin=string.lower(self.txtUsuarioAdmin.GetValue())
                self.passAdmin=self.txtPassAdmin.GetValue()
                self.nomRealAdmin=string.capwords(self.txtNombreRealAdmin.GetValue())
                self.apellidoAdmin=string.capwords(self.txtApellidoAdmin.GetValue())
                self.cargoAdmin=string.capwords(self.txtCargoAdmin.GetValue())
                self.rolAdmin=1

                #se encripta la clave con MD5
                self.hashClave = hashlib.md5()
                self.hashClave.update(self.passAdmin)

                #Validamos que no hayan campos vacios en los datos del Usuario Administrador
                if self.nomAdmin == '' or self.passAdmin == '' or self.nomRealAdmin == '' or self.apellidoAdmin == '' or self.cargoAdmin == '':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.txtUsuarioAdmin.Clear()
                    self.txtPassAdmin.Clear()
                    self.txtNombreRealAdmin.Clear()
                    self.txtApellidoAdmin.Clear()
                    self.txtCargoAdmin.Clear()
                    self.txtUsuarioAdmin.SetFocus()
                    event.Veto()
            #si estamos en la pagina de Preguntas de Seguridad
            elif page==self.wizPageSeguridad and event.GetDirection():
                self.preguntaSeg=self.choicePreguntaSeg.GetStringSelection()
                self.respuestaSeg=self.txtRespPreguntaSeg.GetValue()

                #Validamos que no hayan campos vacios en la pagina de Preguntas de Seguridad
                if self.choicePreguntaSeg.GetSelection() == 0 or self.respuestaSeg == '':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.choicePreguntaSeg.SetSelection(0)
                    self.txtRespPreguntaSeg.Clear()
                    event.Veto()
        except UnicodeEncodeError, e:
            #error, sacamos dialogo y decimos que hagan configuracion -- se crea un LOG del Error
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'La contraseña no debe contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtPassAdmin.Clear()
            self.txtPassAdmin.SetFocus()
            event.Veto()


    def WizardConfigInicialOnWizardFinished( self, event ):
        """
        Al Terminar la carga de Datos de Configuracion
        """
        try:
            #Se conecta con el Servidor de Base de Datos
            BD=ModeloBD()
            #Carga de Registros en la Base de Datos
            BD.configuracionInicial(self.nomAdmin, self.hashClave.hexdigest(), self.nomRealAdmin, self.apellidoAdmin, self.cargoAdmin, self.rolAdmin, self.preguntaSeg, self.respuestaSeg)
            mensaje=wx.MessageDialog(self,u'Configuración Exitosa..!!',"Configurando", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

            #Se abre la Ventana De Login
            self.frameInicio = FInicio(None)
            self.frameInicio.recuperaPass=None

            icon = os.path.normpath(os.path.join(iconDir, "favicon.ico"))
            favicon = wx.Icon(icon, wx.BITMAP_TYPE_ICO, 16, 16)
            wx.Frame.SetIcon(self.frameInicio, favicon)

            self.frameInicio.Show()
            self.frameInicio.txtNomusuario.SetFocus()

        except MySQLdb.Error, e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            #error en la coneccion a la BD, sacamos dialogo y Agregamos al LOG del Sistema
            mensaje=wx.MessageDialog(self,u'Error en la conección a la base de Datos. \nIntente de nuevo o haga click en "Cancelar" para salir. \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtUsuarioAdmin.Clear()
            self.txtPassAdmin.Clear()
            self.txtNombreRealAdmin.Clear()
            self.txtApellidoAdmin.Clear()
            self.txtCargoAdmin.Clear()
            self.choicePreguntaSeg.SetSelection(0)
            self.txtRespPreguntaSeg.Clear()


class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__( self, parent, -1, size=(-1,165), style=wx.LC_REPORT )
        CheckListCtrlMixin.__init__(self)


class NotEmptyValidator(wx.PyValidator):
    """
    Clase para definir un validador de entrada en los TextCtrl y Choices    """

    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return NotEmptyValidator()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        tipo=repr(type(textCtrl))
        if tipo=="<class 'wx._controls.TextCtrl'>": #Si el Control es un TextCtrl
            text = textCtrl.GetValue()
            if len(text) == 0 or text=='(    )    -    ' or text=='        ':
                textCtrl.SetBackgroundColour("red")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx._controls.Choice'>": #Si el Control es un Choice
            text = textCtrl.GetCurrentSelection()
            if text==0.:
                textCtrl.SetBackgroundColour("red")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx._controls.DatePickerCtrl'>": #Si el Control es un DatePickerCtrl
            text = textCtrl.GetValue()
            hoy=wx.DateTime.Today()
            if text > hoy:
                textCtrl.SetBackgroundColour("red")
                textCtrl.SetFocus()
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx.lib.masked.textctrl.TextCtrl'>": #Si el Control es un Masked TextCtrl
            text = textCtrl.GetValue()
            if text=='        ':
                textCtrl.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
                textCtrl.SetBackgroundColour("red")
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True
        elif tipo == "<class 'wx._controls.ComboBox'>": #Si el Control es un ComboBox
            if textCtrl.GetValue() == (u"Seleccione o Ingrese una Institución"):
                textCtrl.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
                textCtrl.SetBackgroundColour("red")
                textCtrl.Refresh()
                return False
            elif textCtrl.IsTextEmpty():
                textCtrl.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
                textCtrl.SetBackgroundColour("red")
                textCtrl.Refresh()
                return False
            else:
                textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
                textCtrl.Refresh()
                return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True


class PanelBienvenida(panelBienvenida):

    pass

class PanelCarga(panelPCarga):

    def mostrarInstituciones(self):
        """
        MUESTRA LAS INSTITUCIONES YA CARGADAS EN EL SISTEMA
        """
        self.comboInstitucion.SetValue(u"Seleccione o Ingrese una Institución")
        inst = app.BD.mostrarInstitucionesDesdeBD()
        if inst:
            for item in inst:
                self.comboInstitucion.Append(string.upper(item[0]))
        else:
            self.comboInstitucion.Append(u'Aún no hay Instituciones Cargadas')

    def comboInstitucionOnTextEnter(self, event):
        inst = app.BD.buscarInstitucion(self.comboInstitucion.GetValue())
        if inst:
            self.comboInstitucion.SetValue(inst[0])


    def cargarDocumento(self):
        """
        Se cargan un  Registro de Correspondencia
        """
        fechaDoc=self.pickerFechaDoc.GetValue().Format('%Y/%m/%d').encode()
        numOficio=self.txtNoficio.GetValue().encode('utf-8')
        fechaR=self.pickerFechaRegistroDoc.GetValue().Format('%Y/%m/%d').encode()
        tipoDoc=string.upper(self.choiceTipoDoc.GetStringSelection().encode('utf-8'))
        remitente=string.upper(self.txtRemitenteDoc.GetValue().encode('utf-8'))
        #institucion=string.upper(self.txtInstitucionDoc.GetValue().encode('utf-8'))

        institucion=string.upper(self.comboInstitucion.GetValue())

        if len(self.txtPautas.GetValue().encode('utf-8'))==0:
            pautas='NINGUNA'
        else:
            pautas=string.upper(self.txtPautas.GetValue().encode('utf-8'))

        asunto=string.upper(self.txtContenidoDoc.GetValue().encode('utf-8'))

        if len(string.upper(self.txtObservDoc.GetValue().encode('utf-8')))==0:
            observ='NINGUNA'
        else:
            observ=string.upper(self.txtObservDoc.GetValue().encode('utf-8'))

        if fechaDoc <= fechaR:
            app.BD.cargarDocumento(institucion, fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,self.GetParent().IdUconectado, pautas)
            mensajeCargado=wx.MessageDialog(self,"Correspondencia Cargada Correctamente.\n\n","Cargada", wx.OK|wx.ICON_INFORMATION)
            mensajeCargado.ShowModal()
            #limpiamos los campos
            self.txtNoficio.Clear()
            self.txtRemitenteDoc.Clear()
            #self.txtInstitucionDoc.Clear()
            self.comboInstitucion.Clear()
            self.txtPautas.Clear()
            self.choiceTipoDoc.SetSelection(0)
            self.pickerFechaDoc.SetValue(wx.DateTime.Today())
            self.pickerFechaRegistroDoc.SetValue(wx.DateTime.Today())
            self.txtContenidoDoc.Clear()
            self.txtObservDoc.Clear()

            self.GetParent().barraHerram.EnableTool(ID_CARGAR, True)
            self.GetParent().cargar.Enable(True)
            self.Hide()
            self.GetParent().bienvenida.Show()
            self.GetParent().Refresh()
        else:
            mensaje=wx.MessageDialog(self,"La Fecha de Registro debe ser Mayor o Igual a la Fecha del Documento.","Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnCargaDocOnButtonClick( self, event ):
        #INICIAMOS VALIDADOR
        self.validator=NotEmptyValidator()

        #VALIDAMOS NUMERO DE OFICIO
        self.validator.SetWindow(self.txtNoficio)
        if self.validator.Validate(self.txtNoficio):
            validaOficio=True
        else:
            validaOficio=False

        #VALIDAMOS TIPO DE DOCUMENTO
        self.validator.SetWindow(self.choiceTipoDoc)
        if self.validator.Validate(self.choiceTipoDoc):
            validaTipoDoc=True
        else:
            validaTipoDoc=False

        #VALIDAMOS REMITENTE
        self.validator.SetWindow(self.txtRemitenteDoc)
        if self.validator.Validate(self.txtRemitenteDoc):
            validaRemitenteDoc=True
        else:
            validaRemitenteDoc=False

        #VALIDAMOS CONTENIDO
        self.validator.SetWindow(self.txtContenidoDoc)
        if self.validator.Validate(self.txtContenidoDoc):
            validaContenidoDoc=True
        else:
            validaContenidoDoc=False

        #VALIDAMOS INSTITUCION
        self.validator.SetWindow(self.comboInstitucion)
        if self.validator.Validate(self.comboInstitucion):
            validaInst=True
        else:
            validaInst=False

        if (validaOficio and validaTipoDoc and validaRemitenteDoc and validaContenidoDoc and validaInst):
            try:
                self.cargarDocumento()
            except MySQLdb.Error, e:
                #agregamos el Error al LOG del Sistema
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                logging.error('%s - [%s]'%(e, trace))
                #error, sacamos dialogo
                app.BD.db.rollback()
                mensaje=wx.MessageDialog(self,"Hubo un Error. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'Los Campos Resaltados son Obligatorios',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

class PanelEdicion(panelPEdicion):

    def mostrarInstituciones(self):
        """
        MUESTRA LAS INSTITUCIONES YA CARGADAS EN EL SISTEMA
        """
        inst = app.BD.mostrarInstitucionesDesdeBD(docId=self.GetParent().doc)
        inst2 = app.BD.mostrarInstitucionesDesdeBD()
        if inst:
            for item in inst:
                self.comboInstitucion.Append(string.upper(item[0]))
                for item2 in inst2:
                    if item != item2:
                        self.comboInstitucion.Append(string.upper(item2[0]))
            self.comboInstitucion.SetSelection(0)

    def comboInstitucionOnTextEnter(self, event):
        inst = app.BD.buscarInstitucion(self.comboInstitucion.GetValue())
        if inst:
            self.comboInstitucion.SetValue(inst[0])

    def actualizarDocumento(self):
        """
        Se Actualizan un registro de Correspondencia
        """
        doc=self.GetParent().doc
        edit=app.BD.editarDocumento(doc)
        inst=app.BD.obtenerInstitucion(edit["Institucion_inst_id"])
        fechaDoc=self.pickerFechaDoc.GetValue().Format('%Y/%m/%d').encode()
        numOficio=self.txtNoficio.GetValue().encode('utf-8')
        fechaR=self.pickerFechaRegistroDoc.GetValue().Format('%Y/%m/%d').encode()
        institucion=string.upper(self.comboInstitucion.GetValue())
        tipoDoc=string.upper(self.choiceTipoDoc.GetStringSelection().encode('utf-8'))
        remitente=string.upper(self.txtRemitenteDoc.GetValue().encode('utf-8'))

        if len(self.txtPautas.GetValue().encode('utf-8'))==0:
            pautas='NINGUNA'
        else:
            pautas=string.upper(self.txtPautas.GetValue().encode('utf-8'))

        asunto=string.upper(self.txtContenidoDoc.GetValue().encode('utf-8'))

        if len(string.upper(self.txtObservDoc.GetValue().encode('utf-8')))==0:
            observ='NINGUNA'
        else:
            observ=string.upper(self.txtObservDoc.GetValue().encode('utf-8'))

        if fechaDoc <= fechaR:
            app.BD.actualizarDocumento(institucion, edit, fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,self.GetParent().IdUconectado,doc, pautas)
            #limpiamos los campos
            self.txtNoficio.Clear()
            self.choiceTipoDoc.SetSelection(0)
            self.pickerFechaDoc.SetValue(wx.DateTime.Today())
            self.pickerFechaRegistroDoc.SetValue(wx.DateTime.Today())
            self.txtRemitenteDoc.Clear()
            self.comboInstitucion.Clear()
            self.txtPautas.Clear()
            self.txtContenidoDoc.Clear()
            self.txtObservDoc.Clear()
            mensajeCargado=wx.MessageDialog(self,"Correspondencia Editada Correctamente.\n\n","Cargada", wx.OK|wx.ICON_INFORMATION)
            mensajeCargado.ShowModal()
            self.GetParent().barraHerram.EnableTool(ID_CARGAR, True)
            self.GetParent().cargar.Enable(True)
            self.Hide()
            self.GetParent().bienvenida.Show()
            self.GetParent().Refresh()
        else:
            mensaje=wx.MessageDialog(self,"La Fecha de Registro debe ser Mayor o Igual a la Fecha del Documento.","Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnEditarDocOnButtonClick( self, event ):
        #INICIAMOS VALIDADOR
        self.validator=NotEmptyValidator()

        #VALIDAMOS NUMERO DE OFICIO
        self.validator.SetWindow(self.txtNoficio)
        if self.validator.Validate(self.txtNoficio):
            validaOficio=True
        else:
            validaOficio=False

        #VALIDAMOS TIPO DE DOCUMENTO
        self.validator.SetWindow(self.choiceTipoDoc)
        if self.validator.Validate(self.choiceTipoDoc):
            validaTipoDoc=True
        else:
            validaTipoDoc=False

        #VALIDAMOS REMITENTE
        self.validator.SetWindow(self.txtRemitenteDoc)
        if self.validator.Validate(self.txtRemitenteDoc):
            validaRemitenteDoc=True
        else:
            validaRemitenteDoc=False

        #VALIDAMOS CONTENIDO
        self.validator.SetWindow(self.txtContenidoDoc)
        if self.validator.Validate(self.txtContenidoDoc):
            validaContenidoDoc=True
        else:
            validaContenidoDoc=False

        if (validaOficio and validaTipoDoc and validaRemitenteDoc and validaContenidoDoc):
            try:
                self.actualizarDocumento()
            except MySQLdb.Error, e:
                #agregamos el Error al LOG del Sistema
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                logging.error('%s - [%s]'%(e, trace))
               #error, sacamos dialogo
                app.BD.db.rollback()
                mensaje=wx.MessageDialog(self,"Hubo un Error. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'Los Campos Resaltados son Obligatorios',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

class FrameBuscar(FrameBusqueda):

    def txtContenidoBusqOnTextEnter(self, event):
        self.cargar()


    def choiceTipoBusquedaOnChoice(self, event):
        """
        Se activan/desactivan controles de busqueda segun el caso
        """
        if self.choiceTipoBusqueda.GetSelection()==0:
            self.txtContenidoBusq.Enable(False)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(False)
        elif self.choiceTipoBusqueda.GetSelection()==1:
            self.txtContenidoBusq.Enable(False)
            self.dateBuscaFechas.Enable(True)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==2:
            self.txtContenidoBusq.Enable(False)
            self.dateBuscaFechas.Enable(True)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==3:
            self.txtContenidoBusq.Enable(True)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==4:
            self.txtContenidoBusq.Enable(True)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==5:
            self.txtContenidoBusq.Enable(True)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==6:
            self.txtContenidoBusq.Enable(True)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==7:
            self.txtContenidoBusq.Enable(True)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(True)
        elif self.choiceTipoBusqueda.GetSelection()==8:
            self.txtContenidoBusq.Enable(False)
            self.dateBuscaFechas.Enable(False)
            self.btnBuscarDoc.Enable(True)

    def btnBuscarDocOnButtonClick( self, event ):
        self.cargar()

    def btnCancelDocOnButtonClick( self, event ):
        self.MakeModal(False)
        self.Close()

    def iniciarListaDocs(self):
        """
        Se muestra la lista de los resultados de busqueda
        """

        self.txtContenidoBusq.Enable(False)
        self.dateBuscaFechas.Enable(False)
        self.btnBuscarDoc.Enable(False)

        #Damos formato a la lista
        self.sizerListaBusqueda = wx.BoxSizer(wx.VERTICAL)
        self.panelListaBusqueda.SetSizer( self.sizerListaBusqueda )

        self.listaBusqueda  = wx.ListCtrl(self.panelListaBusqueda, size=(-1,100),style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.listaBusqueda.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.operacionesDocumento)
        self.listaBusqueda.InsertColumn(0, 'ID ')
        self.listaBusqueda.InsertColumn(1, 'Usuario ')
        self.listaBusqueda.InsertColumn(2, 'Fecha de Registro ')
        self.listaBusqueda.InsertColumn(3, 'Fecha del Documento')
        self.listaBusqueda.InsertColumn(4, u'N° de Oficio')
        self.listaBusqueda.InsertColumn(5, u'Tipo de Documento')
        self.listaBusqueda.InsertColumn(6, 'Remitente')
        self.listaBusqueda.InsertColumn(7, 'Organismo')
        self.listaBusqueda.InsertColumn(8, 'Asunto')
        self.listaBusqueda.InsertColumn(9, 'Pautas')

        #wx.LIST_AUTOSIZE_USEHEADER

        self.listaBusqueda.SetColumnWidth(0, 50)
        self.listaBusqueda.SetColumnWidth(1, 150)
        self.listaBusqueda.SetColumnWidth(2, 120)
        self.listaBusqueda.SetColumnWidth(4, 120)
        self.listaBusqueda.SetColumnWidth(5, 150)
        self.listaBusqueda.SetColumnWidth(6, 150)
        self.listaBusqueda.SetColumnWidth(7, 150)
        self.listaBusqueda.SetColumnWidth(8, 150)
        self.listaBusqueda.SetColumnWidth(9, 150)

        self.sizerListaBusqueda.Add(self.listaBusqueda, 1, wx.EXPAND | wx.TOP, 3)
        self.panelListaBusqueda.Layout()
        self.listaBusqueda.Layout()
        self.listaBusqueda.Refresh()

    def cargarResBusquedaDocs(self):
        #Obtenemos los datos de los Campos
        self.listaBusqueda.Layout()
        contenido=self.txtContenidoBusq.GetValue().encode('utf-8')
        tipo=self.choiceTipoBusqueda.GetStringSelection().encode('utf-8')
        fecha=self.dateBuscaFechas.GetValue().Format('%Y/%m/%d').encode()

        #Obtenemos la lista de documentos de la BD
        lista=app.BD.listarBusquedaDocumentos(tipo, contenido, fecha)


        #Cargamos en la lista, el listado de documentos obtenidos de la BD

        if lista != () :
            for item in lista:
                institucionID=item[13]
                pautaID=item[10]
                institucionNombre=app.BD.obtenerInstitucion(institucionID)
                pautaNombre=app.BD.obtenerPauta(pautaID)
                index = self.listaBusqueda.InsertStringItem(sys.maxint, str(item[0]))
                self.listaBusqueda.SetStringItem(index, 1, str(item[18]))
                self.listaBusqueda.SetStringItem(index, 2, str(item[1]))
                self.listaBusqueda.SetStringItem(index, 3, str(item[2]))
                self.listaBusqueda.SetStringItem(index, 4, item[3])
                self.listaBusqueda.SetStringItem(index, 5, item[4])
                self.listaBusqueda.SetStringItem(index, 6, item[6])
                self.listaBusqueda.SetStringItem(index, 7, unicode(institucionNombre['inst_Nombre']))
                self.listaBusqueda.SetStringItem(index, 8, item[5])
                self.listaBusqueda.SetStringItem(index, 9, unicode(pautaNombre['pau_recibe']))
        else:
            mensaje=wx.MessageDialog(self,u'No hay resultados para esta Busqueda',"Error", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()


    def operacionesDocumento( self, event ):
        """
        Se muestran las opciones disponibles para el documento seleccionado (edicion, eliminacion o vista previa)
        """
        docs=[]
        self.docSel=self.listaBusqueda.GetItemText(self.listaBusqueda.GetFocusedItem())
        usuario_documento=app.BD.obtenerUsuario(self.docSel)

        a= [x[0] for x in usuario_documento]
        for item in a:
            docs.append(item)

        lst = ["Editar", "Eliminar", u"Vista de Impresión del Documento"]
        dlg=wx.SingleChoiceDialog(self, u"Que Operación desea realizar sobre el Documento Seleccionado?", u'Operación',lst,style=wx.CHOICEDLG_STYLE|wx.CENTRE)
        if (dlg.ShowModal() == wx.ID_OK):
            if dlg.GetSelection()==0:
                self.EditarDoc()
                self.Hide()
            if dlg.GetSelection()==1:
                if self.GetParent().IdUconectado in docs:
                    box=wx.MessageDialog(self, "Realmente Desea Eliminar El Registro ?","Advertencia", wx.YES_NO|wx.ICON_QUESTION)
                    if box.ShowModal()==wx.ID_YES:
                        self.EliminarDoc()
                else:
                    mensaje=wx.MessageDialog(self,u"Solo el Usuario que Creó o Editó el Documento puede Realizar esta Acción","Error", wx.OK|wx.ICON_INFORMATION)
                    mensaje.ShowModal()
            if dlg.GetSelection()==2:
                self.MostrarDoc()
            dlg.Destroy()

    def EditarDoc(self):
        """
        Editamos el documento seleccionado
        """
        if self.GetParent().carga.IsShown():
            self.GetParent().carga.Hide()

        self.GetParent().bienvenida.Hide()
        edit=app.BD.editarDocumento(self.docSel)
        inst=app.BD.obtenerInstitucion(edit["Institucion_inst_id"])
        pauta=app.BD.obtenerPauta(edit["doc_id"])

        #Damos formato a la fecha de registro para WxPython
        fechaRegistro = edit['doc_fechaRegistro']
        diaRegistro = fechaRegistro.day
        mesRegistro = fechaRegistro.month
        anioRegistro = fechaRegistro.year
        fechaRegistroFormateada = wx.DateTimeFromDMY(diaRegistro,mesRegistro-1,anioRegistro)

        #Damos formato a la fecha de recepcion para WxPython
        fechaRecep = edit['doc_fechaDocRecep']
        diaRecep = fechaRecep.day
        mesRecep = fechaRecep.month
        anioRecep = fechaRecep.year
        fechaRecepFormateada = wx.DateTimeFromDMY(diaRecep,mesRecep-1,anioRecep)

        self.GetParent().editor=PanelEdicion(self.GetParent())
        self.GetParent().editor.Show()
        self.GetParent().doc=self.docSel
        self.GetParent().editor.mostrarInstituciones()

        self.GetParent().barraHerram.EnableTool(ID_BUSCAR, True)
        self.GetParent().buscar.Enable(True)

        self.GetParent().barraHerram.EnableTool(ID_CARGAR, True)
        self.GetParent().cargar.Enable(True)

        self.MakeModal(False)
        self.Close()
        self.GetParent().Refresh()

        #Cargamos los datos en los campos para edicion desde MySQL

        if edit["doc_Tipo"]=='EMAIL':
            self.GetParent().editor.choiceTipoDoc.SetSelection(1)
        elif edit["doc_Tipo"]=='CARTA':
            self.GetParent().editor.choiceTipoDoc.SetSelection(2)
        elif edit["doc_Tipo"]=='OFICIO':
            self.GetParent().editor.choiceTipoDoc.SetSelection(3)
        elif edit["doc_Tipo"]=='MANUSCRITO':
            self.GetParent().editor.choiceTipoDoc.SetSelection(4)
        elif edit["doc_Tipo"]=='INFORME':
            self.GetParent().editor.choiceTipoDoc.SetSelection(5)
        elif edit["doc_Tipo"]=='SOBRE CERRADO':
            self.GetParent().editor.choiceTipoDoc.SetSelection(6)

        self.GetParent().editor.pickerFechaDoc.SetValue(fechaRecepFormateada)
        self.GetParent().editor.pickerFechaRegistroDoc.SetValue(fechaRegistroFormateada)
        self.GetParent().editor.txtNoficio.SetValue(edit["doc_numOficio"])
        self.GetParent().editor.txtRemitenteDoc.SetValue(edit["doc_Remitente"])
        #self.GetParent().editor.txtInstitucionDoc.SetValue(inst["inst_Nombre"])
        self.GetParent().editor.txtPautas.SetValue(pauta["pau_recibe"])
        self.GetParent().editor.txtContenidoDoc.SetValue(edit["doc_Titulo"])
        self.GetParent().editor.txtObservDoc.SetValue(edit["doc_Observaciones"])

        self.Close()

    def EliminarDoc(self):
        #Eliminamos el Documento seleccionado de la BD
        try:
            app.BD.eliminarDocumentosBD(self.docSel)
            self.listaBusqueda.DeleteItem(self.listaBusqueda.GetFocusedItem())
            mensaje=wx.MessageDialog(self,'Documentos Eliminado..!!',"Eliminando", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()
        except MySQLdb.Error,e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(None,"Hubo un Error Eliminando el Documento. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def MostrarDoc(self):
        """
        Mostramos una vista previa en PDF del documento seleccionado
        """
        ventanaVistaPrevia=FrameReportar(self.GetParent())
        app.IconizarFrames(ventanaVistaPrevia)
        ventanaVistaPrevia.iniciarPanelVistaPrevia()
        ventanaVistaPrevia.Show()
        ventanaVistaPrevia.pdf.LoadFile(app.reporte.CrearVistaPreviaDoc(self.docSel))
        ventanaVistaPrevia.pdf.setView('FitB')
        ventanaVistaPrevia.MakeModal()

    def cargar(self):
        """
        Hacemos la Busqueda
        """
        try:
            self.listaBusqueda.DeleteAllItems()
            self.cargarResBusquedaDocs()
            self.txtContenidoBusq.Clear()
        except MySQLdb.Error, e:
            #agregamos el Error al LOG del Sistema
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
           #error, sacamos dialogo
            app.BD.db.rollback()
            mensaje=wx.MessageDialog(self,"Hubo un Error. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def FrameBusquedaOnClose(self, event):
        """
        Cerramos el Buscador
        """
        self.GetParent().barraHerram.EnableTool(ID_BUSCAR, True)
        self.GetParent().buscar.Enable(True)

        self.GetParent().barraHerram.EnableTool(ID_CARGAR, True)
        self.GetParent().cargar.Enable(True)

        self.MakeModal(False)
        self.Destroy()

class FrameReportar(FrameVPImpresion):
    """
    Clase Hija de FrameVPImpresion, gestiona la vista previa en PDF del Documento Seleccionado
    """
    def iniciarPanelVistaPrevia(self):
        """
        Inicializa el panel para mostrar el control ActiveX PDFWindow que para mostrar documentos PDF generados segun consulta a la Base de datos
        """
        sizer = wx.BoxSizer(wx.VERTICAL)

        #self.pdf = None

        self.pdf = PDFWindow(self.panelVistaPrevia)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.panelVistaPrevia.SetSizer(sizer)
        self.panelVistaPrevia.Layout()


    def FrameVPImpresionOnClose(self, event):
        """
        Cerramos la Vista Previa
        """
        self.GetParent().barraHerram.EnableTool(ID_BUSCAR, True)
        self.GetParent().buscar.Enable(True)

        self.GetParent().barraHerram.EnableTool(ID_CARGAR, True)
        self.GetParent().cargar.Enable(True)
        self.pdf.Close()
        self.MakeModal(False)
        self.Destroy()

class FrameElimUsuarios(FrameEliminarUsuario):
    """
    Clase Hija de FrameEliminarUsuario, gestiona la eliminacion de usuarios del sistema
    """


    def iniciarListaUsuarios(self):
        #Damos formato a la lista
        self.sizerLista = wx.BoxSizer(wx.VERTICAL)
        self.panelListaUsuarios.SetSizer( self.sizerLista )

        self.ListadoUsuarios  = CheckListCtrl(self.panelListaUsuarios)
        self.ListadoUsuarios.InsertColumn(0, 'ID')
        self.ListadoUsuarios.InsertColumn(1, 'Nombre de Usuario')
        self.ListadoUsuarios.InsertColumn(2, 'Nombre Completo')
        self.ListadoUsuarios.InsertColumn(3, 'Cargo')
        self.ListadoUsuarios.InsertColumn(4, 'Rol')

        self.ListadoUsuarios.SetColumnWidth(0, 50)
        self.ListadoUsuarios.SetColumnWidth(1, 150)
        self.ListadoUsuarios.SetColumnWidth(2, 150)
        self.ListadoUsuarios.SetColumnWidth(3, 150)
        self.ListadoUsuarios.SetColumnWidth(4, 150)

        self.sizerLista.Add(self.ListadoUsuarios, 1, wx.EXPAND | wx.TOP, 3)
        self.panelListaUsuarios.Layout()

    def cargarListadoDeUsuarios(self):
        self.ListadoUsuarios.Layout()
        #Obtenemos la lista de usuarios de la BD
        if self.searchUsuarioCtrl.IsEmpty():
            todos=True
            lista=app.BD.listarUsuarios(self.GetParent().IdUconectado,todos)
        else:
            todos=False
            elemento=self.searchUsuarioCtrl.GetValue().encode('utf-8')
            lista=app.BD.listarUsuarios(self.GetParent().IdUconectado,todos,elemento)

        #Cargamos en la lista, el listado de usuarios obtenidos de la BD
        for item in lista:
            index = self.ListadoUsuarios.InsertStringItem(sys.maxint, str(item[0]))
            self.ListadoUsuarios.SetStringItem(index, 1, item[1])
            self.ListadoUsuarios.SetStringItem(index, 2, item[3].decode('utf-8')+' '+item[4].decode('utf-8'))
            self.ListadoUsuarios.SetStringItem(index, 3, item[5])
            if item[6]==1:
                self.ListadoUsuarios.SetStringItem(index, 4, 'Administrador')
            elif item[6]==2:
                self.ListadoUsuarios.SetStringItem(index, 4, 'Usuario Regular')

    def btnCancelElimUsuOnButtonClick( self, event ):
        self.Destroy()

    def selTODOOnButtonClick( self, event ):
        num = self.ListadoUsuarios.GetItemCount()
        for i in range(num):
            self.ListadoUsuarios.CheckItem(i)

    def deSelTodoOnButtonClick( self, event ):
        num = self.ListadoUsuarios.GetItemCount()
        for i in range(num):
            self.ListadoUsuarios.CheckItem(i, False)

    def btnElimUsuarioOnButtonClick( self, event ):
        listaBorrar=[]
        listaBorrados=[]
        num = self.ListadoUsuarios.GetItemCount()
        for i in range(num):
            if self.ListadoUsuarios.IsChecked(i):
                listaBorrar.append(i)
        sorted(listaBorrar)
        listaBorrar.reverse()
        for j in listaBorrar:
            listaBorrados.append(j)
            itemText= self.ListadoUsuarios.GetItemText(j)
            self.ListadoUsuarios.DeleteItem(j)
            #Eliminamos el usuario seleccionado de la BD
            app.BD.eliminarUsuarioBD(itemText)

        mensaje=wx.MessageDialog(self,'Usuario(s) Eliminado(s) %s..!!'%listaBorrados,"Eliminando", wx.OK|wx.ICON_INFORMATION)
        mensaje.ShowModal()

    def cargar(self):
        try:
            self.cargarListadoDeUsuarios()
        except MySQLdb.Error, e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
           #error, sacamos dialogo
            mensaje=wx.MessageDialog(self,"Hubo un Error. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def searchUsuarioCtrlOnSearchButton( self, event ):
        self.ListadoUsuarios.DeleteAllItems()
        self.cargar()

    def searchUsuarioCtrlOnTextEnter( self, event ):
        self.ListadoUsuarios.DeleteAllItems()
        self.cargar()

class AgregaUsuarios(FrameAgregarUsuario):
    """
    Clase Hija de FrameAgregarUsuario, gestiona la adicion de usuarios al sistema
    """

    def btnAddUsuarioOnButtonClick( self, event ):
        #INICIAMOS VALIDADOR
        self.validator=NotEmptyValidator()

        #VALIDAMOS EL NOMBRE DE USUARIO
        self.validator.SetWindow(self.txtNomNUsuario)
        if self.validator.Validate(self.txtNomNUsuario):
            validanNombre=True
        else:
            validanNombre=False

        #VALIDAMOS CONTRASENA
        self.validator.SetWindow(self.txtContrasenaNUsuario)
        if self.validator.Validate(self.txtContrasenaNUsuario):
            validaPass=True
        else:
            validaPass=False

        #VALIDAMOS ROL
        self.validator.SetWindow(self.choiceRolUsuario)
        if self.validator.Validate(self.choiceRolUsuario):
            validaRol=True
        else:
            validaRol=False

        #VALIDAMOS NOMBRE REAL
        self.validator.SetWindow(self.txtNombreRealUsuario)
        if self.validator.Validate(self.txtNombreRealUsuario):
            validaNombreReal=True
        else:
            validaNombreReal=False

        #VALIDAMOS APELLIDO REAL
        self.validator.SetWindow(self.txtApellidoUsuario)
        if self.validator.Validate(self.txtApellidoUsuario):
            validaApellidoUsuario=True
        else:
            validaApellidoUsuario=False

        #VALIDAMOS CARGO
        self.validator.SetWindow(self.txtCargoUsuario)
        if self.validator.Validate(self.txtCargoUsuario):
            validaCargo=True
        else:
            validaCargo=False

        #VALIDAMOS PREGUNTA DE SEGURIDAD
        self.validator.SetWindow(self.choicePreguntaSeg)
        if self.validator.Validate(self.choicePreguntaSeg):
            validaPregunta=True
        else:
            validaPregunta=False

        #VALIDAMOS RESPUESTA DE SEGURIDAD
        self.validator.SetWindow(self.txtRespPreguntaSeg)
        if self.validator.Validate(self.txtRespPreguntaSeg):
            validaRespuesta=True
        else:
            validaRespuesta=False


        try:
            nombre = string.lower(self.txtNomNUsuario.GetValue().encode('utf-8'))
            clave = self.txtContrasenaNUsuario.GetValue()
            rol = self.choiceRolUsuario.GetSelection()
            nombreReal = string.capwords(self.txtNombreRealUsuario.GetValue().encode('utf-8'))
            apellido = string.capwords(self.txtApellidoUsuario.GetValue().encode('utf-8'))
            cargo = string.capitalize(self.txtCargoUsuario.GetValue().encode('utf-8'))
            preguntaSeg=self.choicePreguntaSeg.GetStringSelection()
            respuestaSeg=self.txtRespPreguntaSeg.GetValue().encode('utf-8')

            #Encriptamos la contrasena
            hashClave = hashlib.md5()
            hashClave.update(clave)

            if validanNombre and validaPass and validaRol and validaNombreReal and validaApellidoUsuario and validaCargo and validaPregunta and validaRespuesta:
                try:
                    #Agregamos el Usuario a la BD
                    app.BD.agregarUsuario(nombre,hashClave.hexdigest(),nombreReal,apellido,cargo,rol, preguntaSeg, respuestaSeg)
                    self.txtNomNUsuario.Clear()
                    self.txtContrasenaNUsuario.Clear()
                    self.choiceRolUsuario.SetSelection(0)
                    self.txtNombreRealUsuario.Clear()
                    self.txtApellidoUsuario.Clear()
                    self.txtCargoUsuario.Clear()
                    self.txtNomNUsuario.SetFocus()

                    consultaMasUsuarios=wx.MessageDialog(self, "Desea Agregar mas Usuarios ?", "Agregar otro Usuario", wx.YES_NO|wx.ICON_QUESTION)
                    if consultaMasUsuarios.ShowModal()==wx.ID_NO:
                       self.Close()
                except MySQLdb.Error, e:
                    #agregamos el Error al log del Sistema
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                    logging.error('%s - [%s]'%(e, trace))
                    #error, sacamos dialogo
                    app.BD.db.rollback()
                    mensaje=wx.MessageDialog(self,"Hubo un Error. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
            else:
                mensaje=wx.MessageDialog(self,"Los Campos Resaltados Son Obligtorios !!!","Error", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
        except UnicodeEncodeError, e:
            #error, sacamos dialogo y decimos que hagan configuracion -- se crea un LOG del Error
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'La contraseña no debe contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtContrasenaNUsuario.Clear()
            self.txtContrasenaNUsuario.SetFocus()


    def btnCancelarAddUsuarioOnButtonClick( self, event ):
        self.Destroy()

class FPrincipal(FramePrincipal):
    """
    Class que maneja la interfaz principal del sistema
    """

    def IniciarSizers(self):
        """
        Inicializacion de sizers y Paneles principales (Carga, edicion y bienvenida)
        """
        self.bienvenida=PanelBienvenida(self)

        self.carga=PanelCarga(self)
        self.carga.Hide()

        self.editor=PanelEdicion(self)
        self.editor.Hide()

        app.IconizarFrames(self)

        self.sizerFramePrincipal = wx.BoxSizer( wx.HORIZONTAL )
        self.SetSizer( self.sizerFramePrincipal )
        self.sizerFramePrincipal.Add(self.bienvenida, 1, wx.EXPAND | wx.TOP, 3)
        self.sizerFramePrincipal.Add(self.carga, 1, wx.EXPAND | wx.TOP, 3)
        self.bienvenida.Layout()
        self.Layout()

    def FramePrincipalOnClose(self, event):
        """
        Se cierra la Aplicacion
        """
        self.Destroy()

    def salirOnMenuSelection( self, event ):
        """
        Se cierra la Aplicacion
        """
        box=wx.MessageDialog(self, "Realmente Desea Salir ?","Advertencia", wx.YES_NO|wx.ICON_QUESTION)
        if box.ShowModal()==wx.ID_YES:
            self.Close()

    def eliminarUsuarioOnMenuSelection( self, event ):
        if self.rolUConectado==1:
            ventanaElimUsuarios = FrameElimUsuarios(self)
            app.IconizarFrames(ventanaElimUsuarios)
            ventanaElimUsuarios.Show()
            ventanaElimUsuarios.iniciarListaUsuarios()
        else:
            mensaje=wx.MessageDialog(self,u"Solo el Administrador puede Realizar esta Acción","Error", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

    def agregarUsuarioOnMenuSelection(self, event):
        if self.rolUConectado==1:
            ventanaAgregaUsuarios = AgregaUsuarios(self)
            app.IconizarFrames(ventanaAgregaUsuarios)
            ventanaAgregaUsuarios.Show()
        else:
            mensaje=wx.MessageDialog(self,u"Solo el Administrador puede Realizar esta Acción","Error", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

    def cambiarContraseaOnMenuSelection(self, event):
        ventanaRecordarPass=RecuerdaPass(self)
        ventanaRecordarPass.recuperaPass=False
        app.IconizarFrames(ventanaRecordarPass)
        ventanaRecordarPass.Show()

    def buscarOnMenuSelection( self, event ):
        self.barraHerram.EnableTool(ID_BUSCAR, False)
        self.buscar.Enable(False)

        self.barraHerram.EnableTool(ID_CARGAR, True)
        self.cargar.Enable(True)

        if self.editor.IsShown():
            self.editor.Hide()
        elif self.carga.IsShown():
            self.carga.Hide()

        self.bienvenida.Show()
        self.ventanaBusqueda = FrameBuscar(self)
        app.IconizarFrames(self.ventanaBusqueda)
        self.ventanaBusqueda.Show()
        self.ventanaBusqueda.iniciarListaDocs()
        self.ventanaBusqueda.MakeModal()

    def cargarOnMenuSelection( self, event ):
        self.barraHerram.EnableTool(ID_BUSCAR, True)
        self.buscar.Enable(True)

        self.barraHerram.EnableTool(ID_CARGAR, False)
        self.cargar.Enable(False)

        if self.editor.IsShown():
            self.editor.Hide()
        self.bienvenida.Hide()
        self.carga.mostrarInstituciones()
        self.carga.Show()

    def licenciaOnMenuSelection( self, event ):
        app.IconizarFrames(self)
        licencia = os.path.normpath(os.path.join(licenceDir, "copying"))
        licenseText = open(licencia, "r")
        msg = licenseText.read()
        licenseText.close()
        msg2=wordwrap(msg, 500, wx.ClientDC(self))
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg2, "Licencia")
        dlg.ShowModal()


    def acercaDeOnMenuSelection(self, event):
        app.IconizarFrames(self)
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = u"Sistema de Gestión de Plantilla de Alumnos"
        info.Version = "1.0"
        info.Description = wordwrap(
            u"El Sistema de Gestión Correspondencia permite llevar un control de la misma que se recibe en el Despaho del Director Fundador de la Fundación Musical Simón Bolivar",
            350, wx.ClientDC(self))
        info.WebSite = ("http://www.fesnojiv.gob.ve", u"Página Web FUNDAMUSICAL Bolívar")
        info.Developers = [ "Lic. Mario Castro - mariocastro.pva@gmail.com" ]
        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

class FInicio(FrameInicioSesion):

    def IniciarApp(self):
        self.usuario=self.txtNomusuario.GetValue()
        hashClave = hashlib.md5()
        hashClave.update(self.txtContrasena.GetValue())

        #Verificamos el Usuario Correcto en la BD
        sesion=app.BD.verificaUsuario(self.usuario,hashClave.hexdigest())

        if sesion:
            ventanaPrincipal = FPrincipal(None)
            app.SetTopWindow(ventanaPrincipal)
            ventanaPrincipal.IdUconectado=sesion[0]
            ventanaPrincipal.nomUconectado=sesion[1]
            ventanaPrincipal.rolUConectado=sesion[3]
            ventanaPrincipal.Show()
            ventanaPrincipal.IniciarSizers()
            self.Close()
        else:
            mensajeError=wx.MessageDialog(self, 'Este usuario no existe. \n\n Desea Intentar de nuevo?.',"Error", wx.YES_NO|wx.ICON_QUESTION)
            if mensajeError.ShowModal()==wx.ID_NO:
                self.Close()
            else:
                self.txtNomusuario.Clear()
                self.txtContrasena.Clear()
                self.txtNomusuario.SetFocus()


    def IniciarAplicacionOnButtonClick( self, event ):
        self.IniciarApp()

    def txtContrasenaOnTextEnter(self, event):
        self.IniciarApp()


    def CancelarAplicacionOnButtonClick( self, event ):
        box=wx.MessageDialog(self, "Realmente Desea Salir ?","Advertencia", wx.YES_NO|wx.ICON_QUESTION)
        if box.ShowModal()==wx.ID_YES:
            self.Close()
            event.Skip()

    def FrameInicioSesionOnClose(self,event):
        self.Destroy()

    def btnPassRemOnButtonClick(self, event):
        ventanaRecordarPass=RecuerdaPass(self)
        ventanaRecordarPass.recuperaPass=True
        app.IconizarFrames(ventanaRecordarPass)
        ventanaRecordarPass.Show()


class RecuerdaPass(FrameRecuerdaPass):
    """
    Clase para recuperar contraseñas
    """

    def cambiarPass(self, pregunta, respuesta):
        if self.recuperaPass:
            self.passRecuperado=app.BD.recordarPass(pregunta, respuesta, recupera=True)
        else:
            self.passRecuperado=app.BD.recordarPass(pregunta, respuesta, recupera=False)

        if not self.passRecuperado==None:
            ventanaCambioPass = CambioContrasena(self)
            app.IconizarFrames(ventanaCambioPass)
            ventanaCambioPass.Show()
            ventanaCambioPass.MakeModal()
        else:
            mensaje=wx.MessageDialog(self,u'Respuesta Incorrecta',u"Recuperando Contraseña", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def txtRespPreguntaSegOnTextEnter( self, event ):
        self.cambiarPass(self.choicePreguntaSeg.GetStringSelection(), self.txtRespPreguntaSeg.GetValue())

    def btnAceptarRecuerdaPassOnButtonClick( self, event ):
       self.cambiarPass(self.choicePreguntaSeg.GetStringSelection(), self.txtRespPreguntaSeg.GetValue())

    def btnCancelRecuerdaPassOnButtonClick( self, event ):
        self.Destroy()


class CambioContrasena(FrameCambioContrasena):
    """
    Clase para restablecer contraseñas
    """

    def CambiarContrasena(self, recupera=True):

        if recupera:
            usuario=self.txtNomUsuarioCambioPass.GetValue()
        else:
            usuario=self.GetGrandParent().IdUconectado

        self.clave_nueva=self.txt_contrasenaNueva_Cambio.GetValue()
        hashClaveNueva = hashlib.md5()
        hashClaveNueva.update(self.clave_nueva)

        self.conf_clave_nueva=self.txt_ConfirmaContrasenaNueva_Cambio.GetValue()
        hashConfClaveNueva = hashlib.md5()
        hashConfClaveNueva.update(self.conf_clave_nueva)

        if recupera:
            if app.BD.CambiarClave(usuario, hashClaveNueva.hexdigest(), hashConfClaveNueva.hexdigest()) and usuario==self.GetParent().passRecuperado[0]:
                mensaje=wx.MessageDialog(self,u'Contraseña Modificada',u"Cambiando Contraseña", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
                self.Close()
            else:
                mensaje=wx.MessageDialog(self,u'Contraseña NO Modificada %s'%MySQLdb.Error,u"Error Cambiando Contraseña", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
                self.Close()
        else:
            if app.BD.CambiarClave(usuario, hashClaveNueva.hexdigest(), hashConfClaveNueva.hexdigest(), recupera=False) and usuario==self.GetParent().passRecuperado[0]:
                mensaje=wx.MessageDialog(self,u'Contraseña Modificada',u"Cambiando Contraseña", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
                self.Close()
            else:
                mensaje=wx.MessageDialog(self,u'Contraseña NO Modificada %s'%MySQLdb.Error,u"Error Cambiando Contraseña", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
                self.Close()

    def txt_ConfirmaContrasenaNueva_CambioOnTextEnter(self, event):
        try:
            self.CambiarContrasena(recupera=False)
        except AttributeError:
            self.CambiarContrasena()

    def btnCambioContrasenaOnButtonClick( self, event ):
        try:
            self.CambiarContrasena(recupera=False)
        except AttributeError:
            self.CambiarContrasena()

    def btnCancelaCambioContrasenaOnButtonClick( self, event ):
        self.Close()

    def FrameCambioContrasenaOnClose(self, event):
        self.MakeModal(False)
        self.GetParent().Close()
        self.Destroy()


class App(wx.App):

    def __init__(self, redirect=False, filename='log.log'):
        wx.App.__init__(self, redirect, filename)

    def mostrarSplash(self):
        """
        Muestra un Splash de Bienvenida
        """
        pn = os.path.normpath(os.path.join(bitmapDir, "LogoSistema.jpg"))
        image = wx.Image(pn, wx.BITMAP_TYPE_JPEG)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 3000, None, -1)
        wx.Yield()

    def limpiarDirectorios(self):
        listaDir=os.listdir(tempDir)
        if listaDir != []:
            for item in listaDir:
                if not item=='readme.txt':
                    try:
                        os.remove(os.path.join(tempDir, item))
                    except WindowsError:
                        pass

    def IconizarFrames(self, win):
        icon = os.path.normpath(os.path.join(iconDir, "favicon.ico"))

        favicon = wx.Icon(icon, wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(win, favicon)


    def OnInit(self):

        try:

            self.BD=ModeloBD()
            self.reporte=Reportes()

            self.SetExitOnFrameDelete (True)

            if self.BD.ContarRegistrosAdmin() == 0:
                mywiz = WizardInicio(None)
                mywiz.FitToPage(mywiz.wizPageUsuario)
                mywiz.RunWizard(mywiz.wizPageBD)
                mywiz.Destroy()
            else:
                self.frameInicio = FInicio(None)
                self.frameInicio.recuperaPass=None
                self.IconizarFrames(self.frameInicio)

                self.mostrarSplash()
                self.frameInicio.Show()
                self.frameInicio.txtNomusuario.SetFocus()
            return True
        except MySQLdb.Error,e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(None,"Hubo un Error. %s\n\n" %e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            return False

    def OnExit(self):
        self.limpiarDirectorios()


#LLAMADA PRINCIAPL
if __name__ == '__main__':
    #logging.basicConfig(filename='logSistema.log', filemode='w', format='%(asctime)s : %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    logging.basicConfig(filename='logSistema.log', format='%(asctime)s : %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    app = App(redirect=False)
    app.MainLoop()
