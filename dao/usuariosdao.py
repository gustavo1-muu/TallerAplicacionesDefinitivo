import cx_Oracle
from usuarios import Usuarios
from conexion import Conexion

class UsuariosDao:
    def __init__(self):
        self.conexion = Conexion()
        self.connection = self.conexion.getConexion()
        self.cursor = self.conexion.getCursor()


    def mostrar_usuarios(self):#FUNCIONA BIEN
        query = '''SELECT * FROM usuarios'''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            usuarios = cursor.fetchall()
            for usuarios in usuarios:
                print(f"ID: {usuarios[0]}\nNombre: {usuarios[1]}\nContraseña: {usuarios[2]}\nTipo de usuario: {usuarios[3]}")

        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar areas: {e}") 

    def anadir_usuario(self, id_usuario, nombre_usuario, contrasena_usuario, tipo_usuario):#FUNCIONA BIEN  ---->  !!!IMPORTANTE¡¡¡: LA Ñ SI ES RECONOCIDA POR ORACLE.
     try:
        self.cursor.execute("INSERT INTO Usuarios (ID_Usuarios, Nombre, Contraseña, TipoUsuario) VALUES (:1, :2, :3, :4)", (id_usuario, nombre_usuario, contrasena_usuario, tipo_usuario))
        self.connection.commit()
        print("Usuario agregado exitosamente.")

     except cx_Oracle.Error as error:
        print("Error al agregar el usuario:", error)

    def eliminar_usuario(self, id_usuario):#FUNCIONA BIEN
        try:
            self.cursor.execute("DELETE FROM Usuarios WHERE ID_Usuarios = :1", (id_usuario,))
            self.connection.commit()
            print(f"Usuario con ID {id_usuario} eliminado exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al eliminar el usuario con ID {id_usuario}:", error)

    def editar_usuario(self, id_usuario, nuevo_nombre_usuario, nueva_contrasena, nuevo_tipo_usuario):#FUNCIONA BIEN
        try:
            self.cursor.execute("UPDATE Usuarios SET Nombre = :1, Contraseña = :2, TipoUsuario = :3 WHERE ID_Usuarios = :4", (nuevo_nombre_usuario, nueva_contrasena, nuevo_tipo_usuario, id_usuario))
            self.connection.commit()
            print(f"Usuario con ID {id_usuario} actualizado exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al editar el usuario con ID {id_usuario}:", error)

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()


    def verificar_usuario(self, nombre, contrasena):
        query = '''
            SELECT * FROM usuarios WHERE nombre = :nombre AND Contraseña = :contrasena
        '''
        try:
            
            self.cursor.execute(query, {"nombre": nombre, "contrasena": contrasena})
            usuario = self.cursor.fetchone()
            if usuario:
                usuario_obj = Usuarios(id_usuario=usuario[0], nombre=usuario[1], contrasena=usuario[2], tipo_usuario=usuario[3])
                if usuario_obj.tipo_usuario == 'admin':
                    return 1
                elif usuario_obj.tipo_usuario == 'user':
                    return 2
            else:
                print("Nombre de usuario o contraseña incorrectos.")
        except cx_Oracle.DatabaseError as e:
            print(f"Error al verificar el usuario: {e}")        