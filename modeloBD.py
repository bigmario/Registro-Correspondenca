#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Manejo de Base de Datos Sqlite3 (MODELO)
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
import MySQLdb
import MySQLdb.cursors

class ModeloBD:

    def __init__(self):
        self.conectar()

    def crearBaseDatos(self):
        pass

    def conectarRoot(self):
        try:
            root=frameInicio.txtNomusuario.GetValue()
            pwdRoot=frameInicio.txtContrasena.GetValue()
            self.db = MySQLdb.connect(host='localhost', user=root, passwd=pwdRoot, db='fundamusicalBolivar')
            self.cursor = self.db.cursor()
        except MySQLdb.Error, e:
            #error, sacamos dialogo y decimos que hagan configuracion
            mensaje=wx.MessageDialog(self,"Error en la conección a la base de Datos. \n\n%s \n\nIntente de nuevo." %e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def conectar2(self):
        configBD=[]

        input_file = open("BD_config.txt", "r")
        for line in input_file:
            line = line.strip()
            configBD.append(line)
        input_file.close()

        self.db = MySQLdb.connect(host=configBD[0], user=configBD[1], passwd=configBD[2], db=configBD[3])
        self.cursor = self.db.cursor()

    def conectar(self):
        root="root"
        pwdRoot="macastro"
        self.db = MySQLdb.connect(host='localhost', user=root, passwd=pwdRoot, db='fundamusicalBolivar')
        self.cursor = self.db.cursor()


    def ContarRegistrosAdmin(self):
        """
        Cuenta los registros en la base de datos de administrador
        """
        self.conectar()
        self.cursor.execute("""SELECT COUNT(*) FROM Usuario""")
        resultado=self.cursor.fetchone()
        numero=resultado[0]
        self.desconectar()
        return numero

    def recordarPass(self, pregunta, respuesta, recupera=True):
        self.conectar()
        if recupera:
            self.cursor.execute("""SELECT usu_login FROM Usuario WHERE usu_preguntaSeg=%s and usu_respuestaSeg=%s""", (pregunta, respuesta))
        else:
            self.cursor.execute("""SELECT usu_id FROM Usuario WHERE usu_preguntaSeg=%s and usu_respuestaSeg=%s""", (pregunta, respuesta))
        passRecuperado=self.cursor.fetchone()
        self.desconectar()
        return passRecuperado

    def CambiarClave(self, usuario, clave_nueva, conf_clave_nueva, recupera=True):
        """
        Cambia la Contrasena
        """
        self.conectar()
        try:
            if clave_nueva==conf_clave_nueva:
                if recupera:
                    self.cursor.execute("""UPDATE Usuario SET usu_pwd=%s WHERE usu_login=%s""",(clave_nueva, usuario))
                    self.db.commit()
                else:
                    self.cursor.execute("""UPDATE Usuario SET usu_pwd=%s WHERE usu_id=%s""",(clave_nueva, usuario))
                    self.db.commit()
                return True
            else:
                return False
        except MySQLdb.Error:
            self.db.rollback()
            return False
        finally:
            self.desconectar()

    def configuracionInicial(self, nombreAdmin, passAdmin, nomRealAdmin, apellidoAdmin, cargoAdmin, rolAdmin, preguntaSeg, respuestaSeg):
        self.conectar()
        try:
            self.cursor.execute("""INSERT INTO Usuario (usu_login, usu_pwd, usu_nombre, usu_apellido, usu_cargo, usu_rol, usu_preguntaSeg, usu_respuestaSeg) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", (nombreAdmin, passAdmin, nomRealAdmin, apellidoAdmin, cargoAdmin, rolAdmin, preguntaSeg, respuestaSeg))
            self.db.commit()
        except MySQLdb.Error:
            self.db.rollback()
        finally:
            self.desconectar()

    def verificaUsuario(self, usuario, hashClave):
        self.conectar()
        self.cursor.execute("""SELECT usu_id, usu_login, usu_pwd, usu_rol FROM usuario WHERE usu_login=%s and usu_pwd=%s""",(usuario, hashClave))
        sesion=self.cursor.fetchone()
        self.desconectar()
        return sesion

    def desconectar(self):
        self.db.close()
        self.cursor.close()

    def buscarInstitucion(self, texto):
        """
        SE OBTIENE EL ID Y NOMBRE DE INSTITUCIONES CUYO NOMBRE COINCIDA CO EL TEXTO INGRESADO
        """
        self.conectar()
        self.cursor.execute("""SELECT inst_Nombre FROM institucion WHERE inst_Nombre LIKE %s""", ('%'+texto+'%'))
        id_inst=self.cursor.fetchone()
        self.desconectar()
        return id_inst

    def mostrarInstitucionesDesdeBD(self, docId=None):
        """
        SE OBTIENE EL ID Y NOMBRE DE INSTITUCIONES CUYO NOMBRE COINCIDA CO EL TEXTO INGRESADO
        """
        self.conectar()
        if not docId:
            self.cursor.execute("""SELECT DISTINCT inst_Nombre FROM institucion""")
        else:
            self.cursor.execute("""SELECT DISTINCT inst_Nombre FROM institucion INNER JOIN Documento WHERE documento.doc_id=%s and institucion.inst_id = documento.Institucion_inst_id""", (docId))
        inst_nom=self.cursor.fetchall()
        self.desconectar()
        return inst_nom

    def cargarDocumento(self, institucion, fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,IdUconectado, pautas):
        self.conectar()
        try:
            self.cursor.execute("""SELECT inst_id FROM Institucion WHERE inst_Nombre = %s""", (institucion))
            inst=self.cursor.fetchone()
            if not inst:
                self.cursor.execute("""INSERT INTO Institucion (inst_Nombre) VALUES (%s)""", (institucion))
                id_institucion=self.cursor.lastrowid
                self.cursor.execute("""INSERT INTO Documento (doc_fechaRegistro, doc_fechaDocRecep, doc_numOficio, doc_Tipo, doc_Titulo, doc_Remitente, doc_Observaciones, Institucion_inst_id, Usuario_usu_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,id_institucion,IdUconectado))
            else:
                self.cursor.execute("""SELECT inst_id FROM institucion WHERE inst_Nombre = %s""", (institucion))
                id_institucion=self.cursor.fetchone()
                self.cursor.execute("""INSERT INTO Documento (doc_fechaRegistro, doc_fechaDocRecep, doc_numOficio, doc_Tipo, doc_Titulo, doc_Remitente, doc_Observaciones, Institucion_inst_id, Usuario_usu_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,id_institucion[0],IdUconectado))
            lastId=self.cursor.lastrowid
            self.cursor.execute("""INSERT INTO Pauta (pau_recibe, Documento_doc_id) VALUES (%s,%s)""", (pautas, lastId))
            return self.db.commit()
        except MySQLdb.Error, e:
            print e
            self.db.rollback()
        finally:
            self.desconectar()

    def actualizarDocumento(self,institucion, edit, fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,IdUconectado,doc, pautas):
        self.conectar()
        try:
            #self.cursor.execute("""UPDATE Institucion SET inst_Nombre=%s WHERE inst_id=%s""", (institucion, edit["Institucion_inst_id"]))

            self.cursor.execute("""SELECT inst_id FROM Institucion WHERE inst_Nombre = %s""", (institucion))
            inst=self.cursor.fetchone()
            if not inst:
                self.cursor.execute("""INSERT INTO Institucion (inst_Nombre) VALUES (%s)""", (institucion))
                id_institucion=self.cursor.lastrowid
                self.cursor.execute("""UPDATE Documento SET doc_fechaRegistro=%s, doc_fechaDocRecep=%s, doc_numOficio=%s, doc_Tipo=%s, doc_Titulo=%s, doc_Remitente=%s, doc_Observaciones=%s, Institucion_inst_id=%s, Usuario_usu_id=%s WHERE doc_id=%s""", (fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,id_institucion,IdUconectado,doc))
                self.cursor.execute("""UPDATE Pauta SET pau_recibe=%s, Documento_doc_id=%s WHERE Documento_doc_id=%s""", (pautas, edit["doc_id"],doc))
            else:
                self.cursor.execute("""UPDATE Documento SET doc_fechaRegistro=%s, doc_fechaDocRecep=%s, doc_numOficio=%s, doc_Tipo=%s, doc_Titulo=%s, doc_Remitente=%s, doc_Observaciones=%s, Institucion_inst_id=%s, Usuario_usu_id=%s WHERE doc_id=%s""", (fechaR,fechaDoc,numOficio,tipoDoc,asunto,remitente,observ,inst[0],IdUconectado,doc))
                self.cursor.execute("""UPDATE Pauta SET pau_recibe=%s, Documento_doc_id=%s WHERE Documento_doc_id=%s""", (pautas, edit["doc_id"],doc))
            self.db.commit()
        except MySQLdb.Error:
            self.db.rollback()
        finally:
            self.desconectar()

    def listarBusquedaDocumentos(self, tipo, contenido, fecha, pau=None, insti=None):
        self.conectar()

        if tipo=="Fecha de Registro":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Documento.doc_fechaRegistro = %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", (fecha))
        elif tipo=="Fecha del Documento":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Documento.doc_fechaDocRecep = %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", (fecha))
        elif tipo=="N° de Oficio":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Documento.doc_numOficio LIKE %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", ('%'+contenido+'%'))
        elif tipo=="Remitente":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Documento.doc_Remitente LIKE %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", ('%'+contenido+'%'))
        elif tipo=="Asunto":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Documento.doc_Titulo LIKE %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", ('%'+contenido+'%'))
        elif tipo=="Organismo":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Documento.Institucion_inst_id=Institucion.inst_id AND Institucion.inst_Nombre LIKE %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", ('%'+contenido+'%'))
        elif tipo=="Pautas":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Pauta.Documento_doc_id = Documento.doc_id AND Pauta.pau_recibe LIKE %s AND Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""", ('%'+contenido+'%'))
        elif tipo=="Todos":
            self.cursor.execute("""SELECT DISTINCT * FROM Documento INNER JOIN Pauta INNER JOIN Institucion INNER JOIN Usuario WHERE Pauta.Documento_doc_id=Documento.doc_id AND Documento.Institucion_inst_id=Institucion.inst_id AND Documento.Usuario_usu_id=Usuario.usu_id""")

        listaDocumentos=self.cursor.fetchall()
        self.desconectar()
        return listaDocumentos

    def eliminarDocumentosBD(self,item):
        self.conectar()
        try:
            self.cursor.execute("""DELETE FROM Documento WHERE (doc_id = %s)""", (item))
            #self.cursor.execute("""DELETE FROM Institucion WHERE (Documento_doc_id = %s)""", (item))
            self.cursor.execute("""DELETE FROM Pauta WHERE (Documento_doc_id = %s)""", (item))
            if self.db.commit():
                return True
            else:
                return False
            self.desconectar()
        except MySQLdb.Error:
            self.db.rollback()
        finally:
            self.desconectar()

    def listarUsuarios(self, usuario, todos=None, elemento=None):
        self.conectar()
        if todos:
            self.cursor.execute("""SELECT * FROM Usuario WHERE usu_id != %s""",(usuario))
        else:
            self.cursor.execute("""SELECT * FROM Usuario WHERE ((usu_rol != 1) AND  (usu_login LIKE %s OR usu_nombre LIKE %s OR usu_apellido LIKE %s))""", ('%'+elemento+'%','%'+elemento+'%','%'+elemento+'%'))
        listadoUsuarios=self.cursor.fetchall()
        self.desconectar()
        return listadoUsuarios

    def editarDocumento(self,documento):
        self.conectar()
        query = """SELECT * FROM Documento INNER JOIN Usuario WHERE Documento.doc_id = %s AND Usuario.usu_id=Documento.Usuario_usu_id"""
        c = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        c.execute(query,documento)
        doc = c.fetchone()
        c.close()
        self.desconectar()
        return doc

    def obtenerInstitucion(self,idInst):
        self.conectar()
        query = """SELECT inst_Nombre FROM Institucion WHERE inst_id = %s"""
        c = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        c.execute(query,idInst)
        docInst = c.fetchone()
        c.close()
        self.desconectar()
        return docInst

    def obtenerPauta(self, pautaid):
        self.conectar()
        query = """SELECT pau_recibe FROM Pauta WHERE Documento_doc_id = %s"""
        c = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        c.execute(query,pautaid)
        pauNombre = c.fetchone()
        c.close()
        self.desconectar()
        return pauNombre

    def obtenerUsuario2(self, usuID):
        self.conectar()
        query = """SELECT DISTINCT Documento.Usuario_usu_id, Usuario.usu_login  FROM Documento INNER JOIN Usuario WHERE Usuario_usu_id  = %s AND Documento.Usuario_usu_id = Usuario.usu_id"""
        c = self.db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        c.execute(query,usuID)
        usuario = c.fetchall()
        c.close()
        self.desconectar()
        return usuario

    def obtenerUsuario(self, doc):
        self.conectar()
        query = """SELECT DISTINCT Documento.Usuario_usu_id, Usuario.usu_login  FROM Documento INNER JOIN Usuario WHERE doc_id  = %s AND Documento.Usuario_usu_id = Usuario.usu_id"""
        self.cursor.execute(query,doc)
        usuario = self.cursor.fetchall()
        self.desconectar()
        return usuario

    def eliminarUsuarioBD(self,item):
        self.conectar()
        try:
            self.cursor.execute("""DELETE FROM Usuario WHERE (usu_id = %s)""", (item))
            self.db.commit()
        except MySQLdb.Error:
            self.db.rollback()
        finally:
            self.desconectar()

    def agregarUsuario(self, nombre,hashClave,nombreReal,apellido,cargo,rol, preguntaSeg, respuestaSeg):
        self.conectar()
        try:
            self.cursor.execute("""INSERT INTO Usuario (usu_login, usu_pwd, usu_nombre, usu_apellido, usu_cargo, usu_rol, usu_preguntaSeg, usu_respuestaSeg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""", (nombre,hashClave,nombreReal,apellido,cargo,rol, preguntaSeg, respuestaSeg))
            self.db.commit()
        except MySQLdb.Error:
            self.db.rollback()
        finally:
            self.desconectar()
