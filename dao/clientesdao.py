import cx_Oracle
from clientes import Clientes
from conexion import Conexion

class ClientesDao:

    def __init__(self):
        self.conexion = Conexion()
        self.connection = self.conexion.getConexion()
        self.cursor = self.conexion.getCursor()

    def mostrar_clientes(self):#FUNCIONA BIEN
        query = '''SELECT * FROM clientes'''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            clientes = cursor.fetchall()
            for clientes in clientes:

                print(f"ID: {clientes[0]}\nRut: {clientes[1]}\nNombre: {clientes[2]}\nTelefono: {clientes[3]}\nCorreo: {clientes[4]}")

        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar clientes: {e}") 

    def añadir_clientes(self, id_clientes, rut_cliente, nombre_cliente, telefono_cliente, correo_cliente):#FUNCIONA BIEN
        try:
            self.cursor.execute("INSERT INTO Clientes (ID_Clientes, RutCliente, NombreCliente, TelefonoCliente, CorreoCliente) VALUES (:1, :2, :3, :4, :5)", (id_clientes, rut_cliente, nombre_cliente, telefono_cliente, correo_cliente))
            self.connection.commit()
            print("Cliente agregado exitosamente.")

        except cx_Oracle.Error as error:
            print("Error al agregar el Cliente:", error)

    def eliminar_clientes(self, ID_clientes):#FUNCIONA BIEN
        try:
            self.cursor.execute("DELETE FROM Clientes WHERE ID_Clientes = :1", (ID_clientes,))
            self.connection.commit()
            print(f"Usuario con ID {ID_clientes} eliminado exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al eliminar el usuario con ID {ID_clientes}:", error)

    def editar_clientes(self, ID_clientes, nuevo_rut_cliente ,nuevo_nombre_cliente, nuevo_telefono_cliente, nuevo_correo_cliente):#FUNCIONA BIEN
        try:
            self.cursor.execute("UPDATE Clientes SET RutCliente = :1, NombreCliente = :2, TelefonoCliente = :3, CorreoCliente = :4 WHERE ID_Clientes = :5", (nuevo_rut_cliente , nuevo_nombre_cliente, nuevo_telefono_cliente, nuevo_correo_cliente, ID_clientes))
            self.connection.commit()
            print(f"Usuario con ID {ID_clientes} actualizado exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al editar el usuario con ID {ID_clientes}:", error)