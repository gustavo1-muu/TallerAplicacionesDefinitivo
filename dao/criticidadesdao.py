import cx_Oracle
from criticidades import Criticidades
from conexion import Conexion

class CriticidadesDao:

    def __init__(self):
        self.conexion = Conexion()
        self.connection = self.conexion.getConexion()
        self.cursor = self.conexion.getCursor()

    def mostrar_criticidades(self):#FUNCIONA BIEN
        query = '''SELECT * FROM criticidades'''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            criticidades = cursor.fetchall()
            for criticidades in criticidades:

                print(f"ID: {criticidades[0]}\nNombre: {criticidades[1]}")

        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar areas: {e}") 

    def añadir_criticidades(self, id_criticidad, nombre_criticidad):#FUNCIONA BIEN
        try:
            self.cursor.execute("INSERT INTO Criticidades (ID_Criticidades, NombreCriticidad) VALUES (:1, :2)", (id_criticidad, nombre_criticidad))
            self.connection.commit()
            print("Criticidad agregada exitosamente.")

        except cx_Oracle.Error as error:
            print("Error al agregar la Criticidad:", error)

    def eliminar_criticidades(self, id_criticidad):#FUNCIONA BIEN
        try:
            self.cursor.execute("DELETE FROM Criticidades WHERE ID_Criticidades = :1", (id_criticidad,))
            self.connection.commit()
            print(f"Criticidad con ID {id_criticidad} eliminada exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al eliminar la criticidad con ID {id_criticidad}:", error)

    def editar_criticidades(self, id_criticidad, nuevo_nombre_criticidad):#FUNCIONA BIEN
        try:
            self.cursor.execute("UPDATE Criticidades SET NombreCriticidad = :1 WHERE ID_Criticidades = :2", (nuevo_nombre_criticidad, id_criticidad))
            self.connection.commit()
            print(f"Criticidad con ID {id_criticidad} actualizada exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al editar el área con ID {id_criticidad}:", error)    