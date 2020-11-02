# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.wizard

ID_AGREGAR_USUARIO = 1000
ID_ELIMINAR_USUARIO = 1001
ID_CAMBIAR_CONTRASEA = 1002
ID_SALIR = 1003
ID_CARGAR = 1004
ID_BUSCAR = 1005
ID_LICENCIA = 1006
ID_ACERCA_DE = 1007

###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Registro de Correspondencia FUNDAMUSICAL BOLÍVAR", pos = wx.DefaultPosition, size = wx.Size( 1200,601 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		
		self.menuPrincipal = wx.MenuBar( 0 )
		self.archivo = wx.Menu()
		self.administracin = wx.Menu()
		self.agregarUsuario = wx.MenuItem( self.administracin, ID_AGREGAR_USUARIO, u"Agregar Usuario"+ u"\t" + u"Ctrl+a", u"Agregar Usuario al Sistema", wx.ITEM_NORMAL )
		self.agregarUsuario.SetBitmap( wx.Bitmap( u"icon/userplus32.png", wx.BITMAP_TYPE_ANY ) )
		self.administracin.AppendItem( self.agregarUsuario )
		
		self.eliminarUsuario = wx.MenuItem( self.administracin, ID_ELIMINAR_USUARIO, u"Eliminar Usuario"+ u"\t" + u"Ctrl+e", u"Eliminar Usuario del Sistema", wx.ITEM_NORMAL )
		self.eliminarUsuario.SetBitmap( wx.Bitmap( u"icon/userminus32.png", wx.BITMAP_TYPE_ANY ) )
		self.administracin.AppendItem( self.eliminarUsuario )
		
		self.cambiarContrasea = wx.MenuItem( self.administracin, ID_CAMBIAR_CONTRASEA, u"Cambiar Contraseña"+ u"\t" + u"Ctrl+c", u"Seleccione para Cambiar la Contraseña del Usuario Actual", wx.ITEM_NORMAL )
		self.cambiarContrasea.SetBitmap( wx.Bitmap( u"icon/paperlock32.png", wx.BITMAP_TYPE_ANY ) )
		self.administracin.AppendItem( self.cambiarContrasea )
		
		self.archivo.AppendSubMenu( self.administracin, u"Administración" )
		
		self.archivo.AppendSeparator()
		
		self.salir = wx.MenuItem( self.archivo, ID_SALIR, u"Salir"+ u"\t" + u"Alt+F4", u"Salir de la Aplicación", wx.ITEM_NORMAL )
		self.archivo.AppendItem( self.salir )
		
		self.menuPrincipal.Append( self.archivo, u"Archivo" ) 
		
		self.correspondencia = wx.Menu()
		self.cargar = wx.MenuItem( self.correspondencia, ID_CARGAR, u"Cargar"+ u"\t" + u"Ctrl+l", u"Cargar Nueva Correspondencia", wx.ITEM_NORMAL )
		self.cargar.SetBitmap( wx.Bitmap( u"icon/folderplus32.png", wx.BITMAP_TYPE_ANY ) )
		self.correspondencia.AppendItem( self.cargar )
		
		self.menuPrincipal.Append( self.correspondencia, u"Correspondencia" ) 
		
		self.busqueda = wx.Menu()
		self.buscar = wx.MenuItem( self.busqueda, ID_BUSCAR, u"Buscar Correspondencia"+ u"\t" + u"Ctrl+b", u"Buscar Correspondencia Recibida", wx.ITEM_NORMAL )
		self.buscar.SetBitmap( wx.Bitmap( u"icon/search32.png", wx.BITMAP_TYPE_ANY ) )
		self.busqueda.AppendItem( self.buscar )
		
		self.menuPrincipal.Append( self.busqueda, u"Busqueda" ) 
		
		self.informacin = wx.Menu()
		self.licencia = wx.MenuItem( self.informacin, ID_LICENCIA, u"Licencia"+ u"\t" + u"Ctrl+g", wx.EmptyString, wx.ITEM_NORMAL )
		self.licencia.SetBitmap( wx.Bitmap( u"icon/article32.png", wx.BITMAP_TYPE_ANY ) )
		self.informacin.AppendItem( self.licencia )
		
		self.acercaDe = wx.MenuItem( self.informacin, ID_ACERCA_DE, u"Acerca de.."+ u"\t" + u"Ctrl+u", wx.EmptyString, wx.ITEM_NORMAL )
		self.acercaDe.SetBitmap( wx.Bitmap( u"icon/questionbook32.png", wx.BITMAP_TYPE_ANY ) )
		self.informacin.AppendItem( self.acercaDe )
		
		self.menuPrincipal.Append( self.informacin, u"Información" ) 
		
		self.SetMenuBar( self.menuPrincipal )
		
		self.barraHerram = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.barraHerram.SetToolSeparation( 8 )
		self.barraHerram.AddLabelTool( ID_CARGAR, u"Cargar Correspondencia", wx.Bitmap( u"icon/folderplus32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga Click para Cargar Correspondencia", wx.EmptyString, None ) 
		
		self.barraHerram.AddSeparator()
		
		self.barraHerram.AddLabelTool( ID_BUSCAR, u"Buscar Correspondencia", wx.Bitmap( u"icon/search32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga Click para Buscar Correspondencia", wx.EmptyString, None ) 
		
		self.barraHerram.AddSeparator()
		
		self.barraHerram.Realize() 
		
		self.statusBarPrincipal = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FramePrincipalOnClose )
		self.Bind( wx.EVT_MENU, self.agregarUsuarioOnMenuSelection, id = self.agregarUsuario.GetId() )
		self.Bind( wx.EVT_MENU, self.eliminarUsuarioOnMenuSelection, id = self.eliminarUsuario.GetId() )
		self.Bind( wx.EVT_MENU, self.cambiarContraseaOnMenuSelection, id = self.cambiarContrasea.GetId() )
		self.Bind( wx.EVT_MENU, self.salirOnMenuSelection, id = self.salir.GetId() )
		self.Bind( wx.EVT_MENU, self.cargarOnMenuSelection, id = self.cargar.GetId() )
		self.Bind( wx.EVT_MENU, self.buscarOnMenuSelection, id = self.buscar.GetId() )
		self.Bind( wx.EVT_MENU, self.licenciaOnMenuSelection, id = self.licencia.GetId() )
		self.Bind( wx.EVT_MENU, self.acercaDeOnMenuSelection, id = self.acercaDe.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FramePrincipalOnClose( self, event ):
		event.Skip()
	
	def agregarUsuarioOnMenuSelection( self, event ):
		event.Skip()
	
	def eliminarUsuarioOnMenuSelection( self, event ):
		event.Skip()
	
	def cambiarContraseaOnMenuSelection( self, event ):
		event.Skip()
	
	def salirOnMenuSelection( self, event ):
		event.Skip()
	
	def cargarOnMenuSelection( self, event ):
		event.Skip()
	
	def buscarOnMenuSelection( self, event ):
		event.Skip()
	
	def licenciaOnMenuSelection( self, event ):
		event.Skip()
	
	def acercaDeOnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameInicioSesion
###########################################################################

class FrameInicioSesion ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Iniciar Sesión ", pos = wx.DefaultPosition, size = wx.Size( 494,281 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizerInicioSesion = wx.BoxSizer( wx.VERTICAL )
		
		self.panelPrincipalInicio = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelNombreUsuario = wx.Panel( self.panelPrincipalInicio, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerNombreUsuario = wx.StaticBoxSizer( wx.StaticBox( self.panelNombreUsuario, wx.ID_ANY, u"Nombre de Usuario" ), wx.VERTICAL )
		
		self.txtNomusuario = wx.TextCtrl( self.panelNombreUsuario, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerNombreUsuario.Add( self.txtNomusuario, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelNombreUsuario.SetSizer( sizerNombreUsuario )
		self.panelNombreUsuario.Layout()
		sizerNombreUsuario.Fit( self.panelNombreUsuario )
		bSizer5.Add( self.panelNombreUsuario, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panelContrasena = wx.Panel( self.panelPrincipalInicio, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerContrasena = wx.StaticBoxSizer( wx.StaticBox( self.panelContrasena, wx.ID_ANY, u"Contraseña" ), wx.VERTICAL )
		
		self.txtContrasena = wx.TextCtrl( self.panelContrasena, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		sizerContrasena.Add( self.txtContrasena, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelContrasena.SetSizer( sizerContrasena )
		self.panelContrasena.Layout()
		sizerContrasena.Fit( self.panelContrasena )
		bSizer5.Add( self.panelContrasena, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panelBotonesInicio = wx.Panel( self.panelPrincipalInicio, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.IniciarAplicacion = wx.Button( self.panelBotonesInicio, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.IniciarAplicacion, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.CancelarAplicacion = wx.Button( self.panelBotonesInicio, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.CancelarAplicacion, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.panelBotonesInicio.SetSizer( bSizer46 )
		self.panelBotonesInicio.Layout()
		bSizer46.Fit( self.panelBotonesInicio )
		bSizer5.Add( self.panelBotonesInicio, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_panel33 = wx.Panel( self.panelPrincipalInicio, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		self.btnPassRem = wx.Button( self.m_panel33, wx.ID_ANY, u"Olvidó su Contraseña?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.btnPassRem, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		self.m_panel33.SetSizer( bSizer56 )
		self.m_panel33.Layout()
		bSizer56.Fit( self.m_panel33 )
		bSizer5.Add( self.m_panel33, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelPrincipalInicio.SetSizer( bSizer5 )
		self.panelPrincipalInicio.Layout()
		bSizer5.Fit( self.panelPrincipalInicio )
		bSizerInicioSesion.Add( self.panelPrincipalInicio, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizerInicioSesion )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameInicioSesionOnClose )
		self.txtContrasena.Bind( wx.EVT_TEXT_ENTER, self.txtContrasenaOnTextEnter )
		self.IniciarAplicacion.Bind( wx.EVT_BUTTON, self.IniciarAplicacionOnButtonClick )
		self.CancelarAplicacion.Bind( wx.EVT_BUTTON, self.CancelarAplicacionOnButtonClick )
		self.btnPassRem.Bind( wx.EVT_BUTTON, self.btnPassRemOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameInicioSesionOnClose( self, event ):
		event.Skip()
	
	def txtContrasenaOnTextEnter( self, event ):
		event.Skip()
	
	def IniciarAplicacionOnButtonClick( self, event ):
		event.Skip()
	
	def CancelarAplicacionOnButtonClick( self, event ):
		event.Skip()
	
	def btnPassRemOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameAgregarUsuario
###########################################################################

class FrameAgregarUsuario ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingresar Usuario al Sistema", pos = wx.DefaultPosition, size = wx.Size( 594,546 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerPrincipalAgregarUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel31 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		FrameEdicionCorrespondencia = wx.BoxSizer( wx.VERTICAL )
		
		sizerNombresUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.lblNomRealUsuario = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNomRealUsuario.Wrap( -1 )
		sizerNombresUsuario.Add( self.lblNomRealUsuario, 0, wx.ALL, 5 )
		
		self.txtNombreRealUsuario = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerNombresUsuario.Add( self.txtNombreRealUsuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerNombresUsuario, 0, wx.EXPAND, 5 )
		
		sizerApesUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.lblApellidoUsuario = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Apellido", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblApellidoUsuario.Wrap( -1 )
		sizerApesUsuario.Add( self.lblApellidoUsuario, 0, wx.ALL, 5 )
		
		self.txtApellidoUsuario = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerApesUsuario.Add( self.txtApellidoUsuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerApesUsuario, 0, wx.EXPAND, 5 )
		
		sizerCargoUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.lblCargo = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Cargo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCargo.Wrap( -1 )
		sizerCargoUsuario.Add( self.lblCargo, 0, wx.ALL, 5 )
		
		self.txtCargoUsuario = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerCargoUsuario.Add( self.txtCargoUsuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerCargoUsuario, 0, wx.EXPAND, 5 )
		
		sizerLoginUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.lblNomUsuario = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Nombre de Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNomUsuario.Wrap( -1 )
		sizerLoginUsuario.Add( self.lblNomUsuario, 0, wx.ALL, 5 )
		
		self.txtNomNUsuario = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtNomNUsuario.SetToolTipString( u"Ingrese un nombre de usuario" )
		
		sizerLoginUsuario.Add( self.txtNomNUsuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerLoginUsuario, 0, wx.EXPAND, 5 )
		
		sizerContrasenaUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.lblContrasenaNUsuario = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblContrasenaNUsuario.Wrap( -1 )
		sizerContrasenaUsuario.Add( self.lblContrasenaNUsuario, 0, wx.ALL, 5 )
		
		self.txtContrasenaNUsuario = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sizerContrasenaUsuario.Add( self.txtContrasenaNUsuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerContrasenaUsuario, 0, wx.EXPAND, 5 )
		
		sizerRolUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.lblRolNUsuario = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Rol", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRolNUsuario.Wrap( -1 )
		sizerRolUsuario.Add( self.lblRolNUsuario, 0, wx.ALL, 5 )
		
		choiceRolUsuarioChoices = [ u"Seleccione....", u"Administrador", u"Usuario Regular" ]
		self.choiceRolUsuario = wx.Choice( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceRolUsuarioChoices, 0 )
		self.choiceRolUsuario.SetSelection( 0 )
		sizerRolUsuario.Add( self.choiceRolUsuario, 0, wx.ALL, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerRolUsuario, 0, wx.EXPAND, 5 )
		
		sizerPreguntaSeg = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Escoja una Pregunta de Seguridad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		sizerPreguntaSeg.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Escoja Una Pregunta....", u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		sizerPreguntaSeg.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerPreguntaSeg, 0, wx.EXPAND, 5 )
		
		sizerRespuestaSeg = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText29 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Escriba la respuesta a la pregunta seleccionada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		sizerRespuestaSeg.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.txtRespPreguntaSeg = wx.TextCtrl( self.m_panel31, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		sizerRespuestaSeg.Add( self.txtRespPreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FrameEdicionCorrespondencia.Add( sizerRespuestaSeg, 0, wx.EXPAND, 5 )
		
		
		self.m_panel31.SetSizer( FrameEdicionCorrespondencia )
		self.m_panel31.Layout()
		FrameEdicionCorrespondencia.Fit( self.m_panel31 )
		bSizer62.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel28 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAddUsuario = wx.Button( self.m_panel28, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.btnAddUsuario, 0, wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelarAddUsuario = wx.Button( self.m_panel28, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer55.Add( self.btnCancelarAddUsuario, 0, wx.ALIGN_RIGHT|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel28.SetSizer( bSizer55 )
		self.m_panel28.Layout()
		bSizer55.Fit( self.m_panel28 )
		bSizer62.Add( self.m_panel28, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.m_panel30.SetSizer( bSizer62 )
		self.m_panel30.Layout()
		bSizer62.Fit( self.m_panel30 )
		sizerPrincipalAgregarUsuario.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerPrincipalAgregarUsuario )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtRespPreguntaSeg.Bind( wx.EVT_TEXT_ENTER, self.txtRespPreguntaSegOnTextEnter )
		self.btnAddUsuario.Bind( wx.EVT_BUTTON, self.btnAddUsuarioOnButtonClick )
		self.btnCancelarAddUsuario.Bind( wx.EVT_BUTTON, self.btnCancelarAddUsuarioOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtRespPreguntaSegOnTextEnter( self, event ):
		event.Skip()
	
	def btnAddUsuarioOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarAddUsuarioOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameEliminarUsuario
###########################################################################

class FrameEliminarUsuario ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Busqueda y Eliminación de Usuarios", pos = wx.DefaultPosition, size = wx.Size( 570,316 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerEliminarUsuario = wx.BoxSizer( wx.VERTICAL )
		
		self.panelBusquedaUsuarios = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBusquedaUsuarios = wx.BoxSizer( wx.VERTICAL )
		
		self.searchUsuarioCtrl = wx.SearchCtrl( self.panelBusquedaUsuarios, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		self.searchUsuarioCtrl.ShowSearchButton( True )
		self.searchUsuarioCtrl.ShowCancelButton( False )
		self.searchUsuarioCtrl.SetToolTipString( u"Ingrese el nombre del usuario a buscar" )
		
		sizerBusquedaUsuarios.Add( self.searchUsuarioCtrl, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.panelBusquedaUsuarios.SetSizer( sizerBusquedaUsuarios )
		self.panelBusquedaUsuarios.Layout()
		sizerBusquedaUsuarios.Fit( self.panelBusquedaUsuarios )
		sizerEliminarUsuario.Add( self.panelBusquedaUsuarios, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelListaUsuarios = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		sizerEliminarUsuario.Add( self.panelListaUsuarios, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panelBtnElimusuario = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		siserbotElimUsuario = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnElimUsuario = wx.Button( self.panelBtnElimusuario, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		siserbotElimUsuario.Add( self.btnElimUsuario, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnCancelElimUsu = wx.Button( self.panelBtnElimusuario, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		siserbotElimUsuario.Add( self.btnCancelElimUsu, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		siserbotElimUsuario.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.selTODO = wx.Button( self.panelBtnElimusuario, wx.ID_ANY, u"Seleccionar Todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		siserbotElimUsuario.Add( self.selTODO, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.deSelTodo = wx.Button( self.panelBtnElimusuario, wx.ID_ANY, u"De-Seleccionar Todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		siserbotElimUsuario.Add( self.deSelTodo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.panelBtnElimusuario.SetSizer( siserbotElimUsuario )
		self.panelBtnElimusuario.Layout()
		siserbotElimUsuario.Fit( self.panelBtnElimusuario )
		sizerEliminarUsuario.Add( self.panelBtnElimusuario, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizerEliminarUsuario )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.searchUsuarioCtrl.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchUsuarioCtrlOnSearchButton )
		self.searchUsuarioCtrl.Bind( wx.EVT_TEXT_ENTER, self.searchUsuarioCtrlOnTextEnter )
		self.btnElimUsuario.Bind( wx.EVT_BUTTON, self.btnElimUsuarioOnButtonClick )
		self.btnCancelElimUsu.Bind( wx.EVT_BUTTON, self.btnCancelElimUsuOnButtonClick )
		self.selTODO.Bind( wx.EVT_BUTTON, self.selTODOOnButtonClick )
		self.deSelTodo.Bind( wx.EVT_BUTTON, self.deSelTodoOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def searchUsuarioCtrlOnSearchButton( self, event ):
		event.Skip()
	
	def searchUsuarioCtrlOnTextEnter( self, event ):
		event.Skip()
	
	def btnElimUsuarioOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelElimUsuOnButtonClick( self, event ):
		event.Skip()
	
	def selTODOOnButtonClick( self, event ):
		event.Skip()
	
	def deSelTodoOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameBusqueda
###########################################################################

class FrameBusqueda ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Busqueda de Documentos", pos = wx.DefaultPosition, size = wx.Size( 810,397 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerPrincipalBusquedas = wx.BoxSizer( wx.VERTICAL )
		
		self.panelBuscar = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBuscar = wx.BoxSizer( wx.VERTICAL )
		
		sizerControlesBuscar = wx.StaticBoxSizer( wx.StaticBox( self.panelBuscar, wx.ID_ANY, u"Buscar por:" ), wx.HORIZONTAL )
		
		choiceTipoBusquedaChoices = [ u"Seleccione....", u"Fecha de Registro", u"Fecha del Documento", u"N° de Oficio", u"Remitente", u"Organismo", u"Asunto", u"Pautas", u"Todos" ]
		self.choiceTipoBusqueda = wx.Choice( self.panelBuscar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceTipoBusquedaChoices, 0 )
		self.choiceTipoBusqueda.SetSelection( 0 )
		sizerControlesBuscar.Add( self.choiceTipoBusqueda, 0, wx.ALL, 5 )
		
		self.txtContenidoBusq = wx.TextCtrl( self.panelBuscar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.txtContenidoBusq.SetToolTipString( u"Ingrese el texto a buscar" )
		
		sizerControlesBuscar.Add( self.txtContenidoBusq, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.dateBuscaFechas = wx.DatePickerCtrl( self.panelBuscar, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.dateBuscaFechas.SetToolTipString( u"Utilize esta campo al realizar búsquedas por fecha" )
		
		sizerControlesBuscar.Add( self.dateBuscaFechas, 0, wx.ALL, 5 )
		
		
		sizerBuscar.Add( sizerControlesBuscar, 1, wx.EXPAND, 5 )
		
		self.panelBotBuscar = wx.Panel( self.panelBuscar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBotBuscar = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnBuscarDoc = wx.Button( self.panelBotBuscar, wx.ID_ANY, u"Buscar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBotBuscar.Add( self.btnBuscarDoc, 0, wx.ALL, 5 )
		
		
		self.panelBotBuscar.SetSizer( sizerBotBuscar )
		self.panelBotBuscar.Layout()
		sizerBotBuscar.Fit( self.panelBotBuscar )
		sizerBuscar.Add( self.panelBotBuscar, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.panelBuscar.SetSizer( sizerBuscar )
		self.panelBuscar.Layout()
		sizerBuscar.Fit( self.panelBuscar )
		sizerPrincipalBusquedas.Add( self.panelBuscar, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelResBusqueda = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerResBusqueda = wx.BoxSizer( wx.VERTICAL )
		
		self.panelListaBusqueda = wx.Panel( self.panelResBusqueda, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerResBusqueda.Add( self.panelListaBusqueda, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panelBotListaBusquedas = wx.Panel( self.panelResBusqueda, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBotListaBusqueda = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCancelDoc = wx.Button( self.panelBotListaBusquedas, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerBotListaBusqueda.Add( self.btnCancelDoc, 0, wx.ALL, 5 )
		
		
		self.panelBotListaBusquedas.SetSizer( sizerBotListaBusqueda )
		self.panelBotListaBusquedas.Layout()
		sizerBotListaBusqueda.Fit( self.panelBotListaBusquedas )
		sizerResBusqueda.Add( self.panelBotListaBusquedas, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelResBusqueda.SetSizer( sizerResBusqueda )
		self.panelResBusqueda.Layout()
		sizerResBusqueda.Fit( self.panelResBusqueda )
		sizerPrincipalBusquedas.Add( self.panelResBusqueda, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerPrincipalBusquedas )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameBusquedaOnClose )
		self.choiceTipoBusqueda.Bind( wx.EVT_CHOICE, self.choiceTipoBusquedaOnChoice )
		self.txtContenidoBusq.Bind( wx.EVT_TEXT_ENTER, self.txtContenidoBusqOnTextEnter )
		self.btnBuscarDoc.Bind( wx.EVT_BUTTON, self.btnBuscarDocOnButtonClick )
		self.btnCancelDoc.Bind( wx.EVT_BUTTON, self.btnCancelDocOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameBusquedaOnClose( self, event ):
		event.Skip()
	
	def choiceTipoBusquedaOnChoice( self, event ):
		event.Skip()
	
	def txtContenidoBusqOnTextEnter( self, event ):
		event.Skip()
	
	def btnBuscarDocOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelDocOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameVPImpresion
###########################################################################

class FrameVPImpresion ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Vista Previa de Documento", pos = wx.DefaultPosition, size = wx.Size( 806,474 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelVistaPrevia = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer51.Add( self.panelVistaPrevia, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer51 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameVPImpresionOnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameVPImpresionOnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class panelPCarga
###########################################################################

class panelPCarga ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.Point( -1,-1 ), size = wx.Size( 1190,453 ), style = wx.TAB_TRAVERSAL )
		
		sizerPCarga = wx.BoxSizer( wx.VERTICAL )
		
		self.panelTitulo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self.panelTitulo, wx.ID_ANY, u"Carga de Correspondencia Nueva", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( 12, 74, 90, 92, True, "Arial Black" ) )
		
		bSizer52.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelTitulo.SetSizer( bSizer52 )
		self.panelTitulo.Layout()
		bSizer52.Fit( self.panelTitulo )
		sizerPCarga.Add( self.panelTitulo, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelCargaCorresp = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		sizerCargaDocPrincipal = wx.GridSizer( 1, 2, 0, 0 )
		
		sizerCargaIzq = wx.BoxSizer( wx.VERTICAL )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFechaDoc = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Fecha del Documento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaDoc.Wrap( -1 )
		bSizer25.Add( self.lblFechaDoc, 0, wx.ALL, 5 )
		
		self.pickerFechaDoc = wx.DatePickerCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.pickerFechaDoc.SetToolTipString( u"Indica la fecha de recepción del Documento" )
		
		bSizer25.Add( self.pickerFechaDoc, 0, wx.ALL, 5 )
		
		bSizer2522 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblNOficio = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"N° de Oficio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNOficio.Wrap( -1 )
		bSizer2522.Add( self.lblNOficio, 0, wx.ALL, 5 )
		
		self.txtNoficio = wx.TextCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtNoficio.SetToolTipString( u"Indica el n° de oficio asignado al Documento" )
		
		bSizer2522.Add( self.txtNoficio, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer2522, 1, wx.EXPAND, 5 )
		
		
		sizerCargaIzq.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFechaRegistro = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Fecha de Registro", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaRegistro.Wrap( -1 )
		bSizer27.Add( self.lblFechaRegistro, 0, wx.ALL, 5 )
		
		self.pickerFechaRegistroDoc = wx.DatePickerCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.pickerFechaRegistroDoc.SetToolTipString( u"indica la fecha de registro del Documento en el Sistema" )
		
		bSizer27.Add( self.pickerFechaRegistroDoc, 0, wx.ALL, 5 )
		
		
		sizerCargaIzq.Add( bSizer27, 0, wx.EXPAND, 5 )
		
		bSizer2523 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTipoDoc = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Tipo de Documento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTipoDoc.Wrap( -1 )
		bSizer2523.Add( self.lblTipoDoc, 0, wx.ALL, 5 )
		
		choiceTipoDocChoices = [ u"Seleccione...", u"Email", u"Carta", u"Oficio", u"Manuscrito", u"Informe", u"Sobre Cerrado" ]
		self.choiceTipoDoc = wx.Choice( self.panelCargaCorresp, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceTipoDocChoices, 0 )
		self.choiceTipoDoc.SetSelection( 0 )
		bSizer2523.Add( self.choiceTipoDoc, 0, wx.ALL, 5 )
		
		
		sizerCargaIzq.Add( bSizer2523, 0, wx.EXPAND, 5 )
		
		bSizer252 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblRemitenteDoc = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Remitente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRemitenteDoc.Wrap( -1 )
		bSizer252.Add( self.lblRemitenteDoc, 0, wx.ALL, 5 )
		
		self.txtRemitenteDoc = wx.TextCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtRemitenteDoc.SetToolTipString( u"Indica el Remitente del Documento" )
		
		bSizer252.Add( self.txtRemitenteDoc, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.lblIntitucion = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Institución", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblIntitucion.Wrap( -1 )
		bSizer252.Add( self.lblIntitucion, 0, wx.ALL, 5 )
		
		comboInstitucionChoices = []
		self.comboInstitucion = wx.ComboBox( self.panelCargaCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboInstitucionChoices, wx.TE_PROCESS_ENTER )
		bSizer252.Add( self.comboInstitucion, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerCargaIzq.Add( bSizer252, 0, wx.EXPAND, 5 )
		
		
		sizerCargaDocPrincipal.Add( sizerCargaIzq, 1, wx.EXPAND, 5 )
		
		sizerCargaDer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2524 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblPautas = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Pautas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPautas.Wrap( -1 )
		bSizer2524.Add( self.lblPautas, 0, wx.ALL, 5 )
		
		self.txtPautas = wx.TextCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.txtPautas.SetToolTipString( u"Indica las pautas asignadas al Documento" )
		
		bSizer2524.Add( self.txtPautas, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerCargaDer.Add( bSizer2524, 0, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblContenidoDoc = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Contenido del Documento o Asunto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblContenidoDoc.Wrap( -1 )
		bSizer28.Add( self.lblContenidoDoc, 0, wx.ALL, 5 )
		
		self.txtContenidoDoc = wx.TextCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer28.Add( self.txtContenidoDoc, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerCargaDer.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		bSizer2525 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtObservDoc1 = wx.StaticText( self.panelCargaCorresp, wx.ID_ANY, u"Observaciones", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtObservDoc1.Wrap( -1 )
		bSizer2525.Add( self.txtObservDoc1, 0, wx.ALL, 5 )
		
		self.txtObservDoc = wx.TextCtrl( self.panelCargaCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.txtObservDoc.SetToolTipString( u"Observaciones al documento recibido (opcional)" )
		
		bSizer2525.Add( self.txtObservDoc, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerCargaDer.Add( bSizer2525, 0, wx.EXPAND, 5 )
		
		
		sizerCargaDocPrincipal.Add( sizerCargaDer, 1, wx.EXPAND, 5 )
		
		
		self.panelCargaCorresp.SetSizer( sizerCargaDocPrincipal )
		self.panelCargaCorresp.Layout()
		sizerCargaDocPrincipal.Fit( self.panelCargaCorresp )
		sizerPCarga.Add( self.panelCargaCorresp, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelBotonesCargaDoc = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBotonesCargaDoc = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCargaDoc = wx.Button( self.panelBotonesCargaDoc, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.Size( -1,45 ), 0 )
		self.btnCargaDoc.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnCargaDoc.SetToolTipString( u"Haga Click para Registrar Documento" )
		
		sizerBotonesCargaDoc.Add( self.btnCargaDoc, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelBotonesCargaDoc.SetSizer( sizerBotonesCargaDoc )
		self.panelBotonesCargaDoc.Layout()
		sizerBotonesCargaDoc.Fit( self.panelBotonesCargaDoc )
		sizerPCarga.Add( self.panelBotonesCargaDoc, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerPCarga )
		self.Layout()
		
		# Connect Events
		self.comboInstitucion.Bind( wx.EVT_TEXT_ENTER, self.comboInstitucionOnTextEnter )
		self.btnCargaDoc.Bind( wx.EVT_BUTTON, self.btnCargaDocOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboInstitucionOnTextEnter( self, event ):
		event.Skip()
	
	def btnCargaDocOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class panelBienvenida
###########################################################################

class panelBienvenida ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 790,474 ), style = wx.TAB_TRAVERSAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel25 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel26 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel26, wx.ID_ANY, wx.Bitmap( u"bitmaps/cabecera.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel26.SetSizer( bSizer43 )
		self.m_panel26.Layout()
		bSizer43.Fit( self.m_panel26 )
		bSizer42.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer42.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel27 = wx.Panel( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel24.SetSizer( bSizer42 )
		self.m_panel24.Layout()
		bSizer42.Fit( self.m_panel24 )
		bSizer41.Add( self.m_panel24, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class panelPEdicion
###########################################################################

class panelPEdicion ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.Point( -1,-1 ), size = wx.Size( 1190,453 ), style = wx.TAB_TRAVERSAL )
		
		sizerPCarga = wx.BoxSizer( wx.VERTICAL )
		
		self.panelTitulo = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText25 = wx.StaticText( self.panelTitulo, wx.ID_ANY, u"Edición de Correspondencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( 12, 74, 90, 92, True, "Arial Black" ) )
		
		bSizer52.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelTitulo.SetSizer( bSizer52 )
		self.panelTitulo.Layout()
		bSizer52.Fit( self.panelTitulo )
		sizerPCarga.Add( self.panelTitulo, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelEdicionCorresp = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.RAISED_BORDER|wx.TAB_TRAVERSAL )
		sizerCargaDocPrincipal = wx.GridSizer( 1, 2, 0, 0 )
		
		sizerEdicionIzq = wx.BoxSizer( wx.VERTICAL )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFechaDoc = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Fecha del Documento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaDoc.Wrap( -1 )
		bSizer25.Add( self.lblFechaDoc, 0, wx.ALL, 5 )
		
		self.pickerFechaDoc = wx.DatePickerCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.pickerFechaDoc.SetToolTipString( u"Indica la fecha de recepción del Documento" )
		
		bSizer25.Add( self.pickerFechaDoc, 0, wx.ALL, 5 )
		
		bSizer2522 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblNOficio = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"N° de Oficio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNOficio.Wrap( -1 )
		bSizer2522.Add( self.lblNOficio, 0, wx.ALL, 5 )
		
		self.txtNoficio = wx.TextCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtNoficio.SetToolTipString( u"Indica el n° de oficio asignado al Documento" )
		
		bSizer2522.Add( self.txtNoficio, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer2522, 1, wx.EXPAND, 5 )
		
		
		sizerEdicionIzq.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFechaRegistro = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Fecha de Registro", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaRegistro.Wrap( -1 )
		bSizer27.Add( self.lblFechaRegistro, 0, wx.ALL, 5 )
		
		self.pickerFechaRegistroDoc = wx.DatePickerCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.pickerFechaRegistroDoc.SetToolTipString( u"indica la fecha de registro del Documento en el Sistema" )
		
		bSizer27.Add( self.pickerFechaRegistroDoc, 0, wx.ALL, 5 )
		
		
		sizerEdicionIzq.Add( bSizer27, 0, wx.EXPAND, 5 )
		
		bSizer2523 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTipoDoc = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Tipo de Documento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTipoDoc.Wrap( -1 )
		bSizer2523.Add( self.lblTipoDoc, 0, wx.ALL, 5 )
		
		choiceTipoDocChoices = [ u"Seleccione...", u"Email", u"Carta", u"Oficio", u"Manuscrito", u"Informe", u"Sobre Cerrado" ]
		self.choiceTipoDoc = wx.Choice( self.panelEdicionCorresp, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceTipoDocChoices, 0 )
		self.choiceTipoDoc.SetSelection( 0 )
		bSizer2523.Add( self.choiceTipoDoc, 0, wx.ALL, 5 )
		
		
		sizerEdicionIzq.Add( bSizer2523, 0, wx.EXPAND, 5 )
		
		bSizer252 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblRemitenteDoc = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Remitente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRemitenteDoc.Wrap( -1 )
		bSizer252.Add( self.lblRemitenteDoc, 0, wx.ALL, 5 )
		
		self.txtRemitenteDoc = wx.TextCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtRemitenteDoc.SetToolTipString( u"Indica el Remitente del Documento" )
		
		bSizer252.Add( self.txtRemitenteDoc, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.lblIntitucion = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Institución", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblIntitucion.Wrap( -1 )
		bSizer252.Add( self.lblIntitucion, 0, wx.ALL, 5 )
		
		comboInstitucionChoices = []
		self.comboInstitucion = wx.ComboBox( self.panelEdicionCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, comboInstitucionChoices, wx.TE_PROCESS_ENTER )
		bSizer252.Add( self.comboInstitucion, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerEdicionIzq.Add( bSizer252, 0, wx.EXPAND, 5 )
		
		
		sizerCargaDocPrincipal.Add( sizerEdicionIzq, 1, wx.EXPAND, 5 )
		
		sizerEdicionDer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2524 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblPautas = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Pautas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPautas.Wrap( -1 )
		bSizer2524.Add( self.lblPautas, 0, wx.ALL, 5 )
		
		self.txtPautas = wx.TextCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.txtPautas.SetToolTipString( u"Indica las pautas asignadas al Documento" )
		
		bSizer2524.Add( self.txtPautas, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerEdicionDer.Add( bSizer2524, 0, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblContenidoDoc = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Contenido del Documento o Asunto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblContenidoDoc.Wrap( -1 )
		bSizer28.Add( self.lblContenidoDoc, 0, wx.ALL, 5 )
		
		self.txtContenidoDoc = wx.TextCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer28.Add( self.txtContenidoDoc, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerEdicionDer.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		bSizer2525 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtObservDoc1 = wx.StaticText( self.panelEdicionCorresp, wx.ID_ANY, u"Observaciones", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtObservDoc1.Wrap( -1 )
		bSizer2525.Add( self.txtObservDoc1, 0, wx.ALL, 5 )
		
		self.txtObservDoc = wx.TextCtrl( self.panelEdicionCorresp, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.txtObservDoc.SetToolTipString( u"Observaciones al documento recibido (opcional)" )
		
		bSizer2525.Add( self.txtObservDoc, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerEdicionDer.Add( bSizer2525, 0, wx.EXPAND, 5 )
		
		
		sizerCargaDocPrincipal.Add( sizerEdicionDer, 1, wx.EXPAND, 5 )
		
		
		self.panelEdicionCorresp.SetSizer( sizerCargaDocPrincipal )
		self.panelEdicionCorresp.Layout()
		sizerCargaDocPrincipal.Fit( self.panelEdicionCorresp )
		sizerPCarga.Add( self.panelEdicionCorresp, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelBotonesEdicionDoc = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBotonesEdicionDoc = wx.BoxSizer( wx.VERTICAL )
		
		self.btnEditarDoc = wx.Button( self.panelBotonesEdicionDoc, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.Size( -1,45 ), 0 )
		self.btnEditarDoc.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.btnEditarDoc.SetToolTipString( u"Haga Click para Registrar Documento" )
		
		sizerBotonesEdicionDoc.Add( self.btnEditarDoc, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelBotonesEdicionDoc.SetSizer( sizerBotonesEdicionDoc )
		self.panelBotonesEdicionDoc.Layout()
		sizerBotonesEdicionDoc.Fit( self.panelBotonesEdicionDoc )
		sizerPCarga.Add( self.panelBotonesEdicionDoc, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerPCarga )
		self.Layout()
		
		# Connect Events
		self.comboInstitucion.Bind( wx.EVT_TEXT_ENTER, self.comboInstitucionOnTextEnter )
		self.btnEditarDoc.Bind( wx.EVT_BUTTON, self.btnEditarDocOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def comboInstitucionOnTextEnter( self, event ):
		event.Skip()
	
	def btnEditarDocOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class WizardConfigInicial
###########################################################################

class WizardConfigInicial ( wx.wizard.Wizard ):
	
	def __init__( self, parent ):
		wx.wizard.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuración Inicial", bitmap = wx.Bitmap( u"bitmaps/logoWizard.png", wx.BITMAP_TYPE_ANY ), pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( 567,482 ), wx.DefaultSize )
		self.m_pages = []
		
		self.wizPageUsuario = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.wizPageUsuario )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel30 = wx.Panel( self.wizPageUsuario, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer57 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel27 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel27, wx.ID_ANY, u"Nombre de Usuario Administrador" ), wx.VERTICAL )
		
		self.txtUsuarioAdmin = wx.TextCtrl( self.m_panel27, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.txtUsuarioAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel27.SetSizer( sbSizer8 )
		self.m_panel27.Layout()
		sbSizer8.Fit( self.m_panel27 )
		bSizer57.Add( self.m_panel27, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel28 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel28, wx.ID_ANY, u"Contraseña Administrador" ), wx.VERTICAL )
		
		self.txtPassAdmin = wx.TextCtrl( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer9.Add( self.txtPassAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel28.SetSizer( sbSizer9 )
		self.m_panel28.Layout()
		sbSizer9.Fit( self.m_panel28 )
		bSizer57.Add( self.m_panel28, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel33 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel33, wx.ID_ANY, u"Nombre" ), wx.VERTICAL )
		
		self.txtNombreRealAdmin = wx.TextCtrl( self.m_panel33, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer14.Add( self.txtNombreRealAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel33.SetSizer( sbSizer14 )
		self.m_panel33.Layout()
		sbSizer14.Fit( self.m_panel33 )
		bSizer57.Add( self.m_panel33, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel34 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel34, wx.ID_ANY, u"Apellido" ), wx.VERTICAL )
		
		self.txtApellidoAdmin = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.txtApellidoAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel34.SetSizer( sbSizer15 )
		self.m_panel34.Layout()
		sbSizer15.Fit( self.m_panel34 )
		bSizer57.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel35 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel35, wx.ID_ANY, u"Cargo" ), wx.VERTICAL )
		
		self.txtCargoAdmin = wx.TextCtrl( self.m_panel35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer16.Add( self.txtCargoAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel35.SetSizer( sbSizer16 )
		self.m_panel35.Layout()
		sbSizer16.Fit( self.m_panel35 )
		bSizer57.Add( self.m_panel35, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel30.SetSizer( bSizer57 )
		self.m_panel30.Layout()
		bSizer57.Fit( self.m_panel30 )
		bSizer54.Add( self.m_panel30, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.wizPageUsuario.SetSizer( bSizer54 )
		self.wizPageUsuario.Layout()
		self.wizPageSeguridad = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.wizPageSeguridad )
		
		bSizer69 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel341 = wx.Panel( self.wizPageSeguridad, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer58 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel36 = wx.Panel( self.m_panel341, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Escoja una Pregunta de Seguridad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer59.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Seleccione......", u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		bSizer59.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel36.SetSizer( bSizer59 )
		self.m_panel36.Layout()
		bSizer59.Fit( self.m_panel36 )
		bSizer58.Add( self.m_panel36, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel37 = wx.Panel( self.m_panel341, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText29 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Escriba la respuesta a la pregunta seleccionada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer60.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.txtRespPreguntaSeg = wx.TextCtrl( self.m_panel37, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.txtRespPreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel37.SetSizer( bSizer60 )
		self.m_panel37.Layout()
		bSizer60.Fit( self.m_panel37 )
		bSizer58.Add( self.m_panel37, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel341.SetSizer( bSizer58 )
		self.m_panel341.Layout()
		bSizer58.Fit( self.m_panel341 )
		bSizer69.Add( self.m_panel341, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.wizPageSeguridad.SetSizer( bSizer69 )
		self.wizPageSeguridad.Layout()
		self.wizPageResumen = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.wizPageResumen )
		
		bSizer74 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel50 = wx.Panel( self.wizPageResumen, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer74.Add( self.m_panel50, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.wizPageResumen.SetSizer( bSizer74 )
		self.wizPageResumen.Layout()
		bSizer74.Fit( self.wizPageResumen )
		self.Centre( wx.BOTH )
		
		
		# Connect Events
		self.Bind( wx.wizard.EVT_WIZARD_CANCEL, self.WizardConfigInicialOnWizardCancel )
		self.Bind( wx.wizard.EVT_WIZARD_FINISHED, self.WizardConfigInicialOnWizardFinished )
		self.Bind( wx.wizard.EVT_WIZARD_PAGE_CHANGED, self.WizardConfigInicialOnWizardPageChanged )
		self.Bind( wx.wizard.EVT_WIZARD_PAGE_CHANGING, self.WizardConfigInicialOnWizardPageChanging )
	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def WizardConfigInicialOnWizardCancel( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardFinished( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardPageChanged( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardPageChanging( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameRecuerdaPass
###########################################################################

class FrameRecuerdaPass ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Recuperación de Contraseña", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer57 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel34 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer58 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel36 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText28 = wx.StaticText( self.m_panel36, wx.ID_ANY, u"Escoja una Pregunta de Seguridad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer59.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.m_panel36, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		bSizer59.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel36.SetSizer( bSizer59 )
		self.m_panel36.Layout()
		bSizer59.Fit( self.m_panel36 )
		bSizer58.Add( self.m_panel36, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel37 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText29 = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Escriba la respuesta a la pregunta seleccionada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer60.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.txtRespPreguntaSeg = wx.TextCtrl( self.m_panel37, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer60.Add( self.txtRespPreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel37.SetSizer( bSizer60 )
		self.m_panel37.Layout()
		bSizer60.Fit( self.m_panel37 )
		bSizer58.Add( self.m_panel37, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel34.SetSizer( bSizer58 )
		self.m_panel34.Layout()
		bSizer58.Fit( self.m_panel34 )
		bSizer57.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel35 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel39 = wx.Panel( self.m_panel35, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAceptarRecuerdaPass = wx.Button( self.m_panel39, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.btnAceptarRecuerdaPass, 0, wx.ALL, 5 )
		
		self.btnCancelRecuerdaPass = wx.Button( self.m_panel39, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62.Add( self.btnCancelRecuerdaPass, 0, wx.ALL, 5 )
		
		
		self.m_panel39.SetSizer( bSizer62 )
		self.m_panel39.Layout()
		bSizer62.Fit( self.m_panel39 )
		bSizer61.Add( self.m_panel39, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel35.SetSizer( bSizer61 )
		self.m_panel35.Layout()
		bSizer61.Fit( self.m_panel35 )
		bSizer57.Add( self.m_panel35, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer57 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtRespPreguntaSeg.Bind( wx.EVT_TEXT_ENTER, self.txtRespPreguntaSegOnTextEnter )
		self.btnAceptarRecuerdaPass.Bind( wx.EVT_BUTTON, self.btnAceptarRecuerdaPassOnButtonClick )
		self.btnCancelRecuerdaPass.Bind( wx.EVT_BUTTON, self.btnCancelRecuerdaPassOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtRespPreguntaSegOnTextEnter( self, event ):
		event.Skip()
	
	def btnAceptarRecuerdaPassOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelRecuerdaPassOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameCambioContrasena
###########################################################################

class FrameCambioContrasena ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Restablecimiento de Contraseña", pos = wx.DefaultPosition, size = wx.Size( 500,252 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer73 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel50 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer74 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel50, wx.ID_ANY, u"Nombre de Usuario" ), wx.VERTICAL )
		
		self.txtNomUsuarioCambioPass = wx.TextCtrl( self.m_panel50, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer17.Add( self.txtNomUsuarioCambioPass, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer74.Add( sbSizer17, 0, wx.EXPAND, 5 )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel50, wx.ID_ANY, u"Nueva Contraseña" ), wx.VERTICAL )
		
		self.txt_contrasenaNueva_Cambio = wx.TextCtrl( self.m_panel50, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer14.Add( self.txt_contrasenaNueva_Cambio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer74.Add( sbSizer14, 0, wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel50, wx.ID_ANY, u"Confirme Contraseña" ), wx.VERTICAL )
		
		self.txt_ConfirmaContrasenaNueva_Cambio = wx.TextCtrl( self.m_panel50, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		sbSizer15.Add( self.txt_ConfirmaContrasenaNueva_Cambio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer74.Add( sbSizer15, 0, wx.EXPAND, 5 )
		
		bSizer75 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel51 = wx.Panel( self.m_panel50, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer76 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCambioContrasena = wx.Button( self.m_panel51, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76.Add( self.btnCambioContrasena, 0, wx.ALL, 5 )
		
		self.btnCancelaCambioContrasena = wx.Button( self.m_panel51, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76.Add( self.btnCancelaCambioContrasena, 0, wx.ALL, 5 )
		
		
		self.m_panel51.SetSizer( bSizer76 )
		self.m_panel51.Layout()
		bSizer76.Fit( self.m_panel51 )
		bSizer75.Add( self.m_panel51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer74.Add( bSizer75, 0, wx.EXPAND, 5 )
		
		
		self.m_panel50.SetSizer( bSizer74 )
		self.m_panel50.Layout()
		bSizer74.Fit( self.m_panel50 )
		bSizer73.Add( self.m_panel50, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer73 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameCambioContrasenaOnClose )
		self.txt_ConfirmaContrasenaNueva_Cambio.Bind( wx.EVT_TEXT_ENTER, self.txt_ConfirmaContrasenaNueva_CambioOnTextEnter )
		self.btnCambioContrasena.Bind( wx.EVT_BUTTON, self.btnCambioContrasenaOnButtonClick )
		self.btnCancelaCambioContrasena.Bind( wx.EVT_BUTTON, self.btnCancelaCambioContrasenaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameCambioContrasenaOnClose( self, event ):
		event.Skip()
	
	def txt_ConfirmaContrasenaNueva_CambioOnTextEnter( self, event ):
		event.Skip()
	
	def btnCambioContrasenaOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelaCambioContrasenaOnButtonClick( self, event ):
		event.Skip()
	

