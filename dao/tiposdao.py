import cx_Oracle
from tipos import Tipos
from conexion import Conexion

class TiposDao:
    def __init__(self):
        self.conexion = Conexion()
        self.connection = self.conexion.getConexion()
        self.cursor = self.conexion.getCursor()

    def mostrar_tipos(self):#FUNCIONA BIEN
        query = '''SELECT * FROM tipos'''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            tipos = cursor.fetchall()
            for tipos in tipos:

                print(f"ID: {tipos[0]}\nNombre: {tipos[1]}")

        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar Tipos de tiquet: {e}") 

    def anadir_tipos(self, id_tipotiquet, nombre_tipotiquet):#FUNCIONA BIEN
        try:
            self.cursor.execute("INSERT INTO Tipos (ID_TipoTiquet, TipoTiquet) VALUES (:1, :2)", (id_tipotiquet, nombre_tipotiquet))
            self.connection.commit()
            print("Tipo de Tiquet agregado exitosamente.")

        except cx_Oracle.Error as error:
            print("Error al agregar el Tipo de Tiquet:", error)

    def eliminar_tipos(self, id_tipotiquet):#FUNCIONA BIEN
        try:
            self.cursor.execute("DELETE FROM Tipos WHERE ID_TipoTiquet = :1", (id_tipotiquet,))
            self.connection.commit()
            print(f"Tipo de Tiquet con ID {id_tipotiquet} eliminado exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al eliminar el Tipo de Tiquet con ID {id_tipotiquet}:", error)

    def editar_tipos(self, id_tipotiquet, nuevo_nombre_tipotiquet):#FUNCIONA BIEN
        try:
            self.cursor.execute("UPDATE Tipos SET TipoTiquet = :1 WHERE ID_TipoTiquet = :2", (nuevo_nombre_tipotiquet, id_tipotiquet))
            self.connection.commit()
            print(f"El Tipo de Tiquet con ID {id_tipotiquet} actualizada exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al editar el Tipo de Tiquet con ID {id_tipotiquet}:", error) 