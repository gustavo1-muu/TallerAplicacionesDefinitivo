import cx_Oracle
from areas import Areas
from conexion import Conexion

class AreasDao:
    def __init__(self):
        self.conexion = Conexion()
        self.connection = self.conexion.getConexion()
        self.cursor = self.conexion.getCursor()

    # TODAS LOS MÉTODOS FUNCIONAN#
    def mostrar_areas(self):
        query = '''SELECT * FROM areas'''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            areas = cursor.fetchall()
            for areas in areas:

                print(f"ID: {areas[0]}\nNombre: {areas[1]}")

        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar areas: {e}") 

    def añadir_area(self, id_area, nombre_area):
        try:
            self.cursor.execute("INSERT INTO Areas (ID_Areas, NombreArea) VALUES (:1, :2)", (id_area, nombre_area))
            self.connection.commit()
            print("Área agregada exitosamente.")

        except cx_Oracle.Error as error:
            print("Error al agregar el área:", error)

    def eliminar_area(self, id_area):
        try:
            self.cursor.execute("DELETE FROM Areas WHERE ID_Areas = :1", (id_area,))
            self.connection.commit()
            print(f"Área con ID {id_area} eliminada exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al eliminar el área con ID {id_area}:", error)

    def editar_area(self, id_area, nuevo_nombre_area):
        try:
            self.cursor.execute("UPDATE Areas SET NombreArea = :1 WHERE ID_Areas = :2", (nuevo_nombre_area, id_area))
            self.connection.commit()
            print(f"Área con ID {id_area} actualizada exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al editar el área con ID {id_area}:", error)
            
    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
