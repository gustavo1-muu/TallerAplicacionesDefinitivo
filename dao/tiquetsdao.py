import cx_Oracle
from tiquets import Tiquets
from conexion import Conexion

class TiquetDao:
    def __init__(self):
        self.conexion = Conexion()
        self.connection = self.conexion.getConexion()
        self.cursor = self.conexion.getCursor()

    def mostrar_tiquets(self):#HAY QUE MODIFICARLA DE AHI
        query = '''SELECT * FROM tiquet'''
        try:
            cursor = self.conexion.getCursor()
            cursor.execute(query)
            tiquet = cursor.fetchall()
            print("Tiquets:")
            for tiquet in tiquet:
                
                print(f"\nID: {tiquet[0]}\nUsuario Creador: {tiquet[1]}\nUsuario Asignado: {tiquet[2]}\nCliente Asignado: {tiquet[3]}\nTipo Tiquet: {tiquet[4]}\nCriticidad: {tiquet[5]}\nÁrea Destino: {tiquet[6]}\nDetalles de Servicio: {tiquet[7]}\nDetalles de Problema: {tiquet[8]}\nEstado: {tiquet[9]}\nObservacion: {tiquet[10]}\n")

        except cx_Oracle.DatabaseError as e:
            print(f"Error al mostrar Tiquets: {e}") 

    def anadir_tiquet(self, id_tiquet, id_usuario_creador, id_usuario_asignado, id_cliente_asignado, id_tipo_tiquet, id_criticidad, id_area_destino, detalles_servicio, detalles_problema, estado, observaciones):#FUNCIONA BIEN
        try:
            self.cursor.execute("INSERT INTO Tiquet (ID_Tiquet, ID_UsuarioCreador, ID_UsuarioAsignado, ID_ClienteAsignado, ID_TipoTiquet, ID_Criticidad, ID_AreaDestino, DetalleServicio, DetalleProblema, Estado, Observacion) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)", (id_tiquet, id_usuario_creador, id_usuario_asignado, id_cliente_asignado, id_tipo_tiquet, id_criticidad, id_area_destino, detalles_servicio, detalles_problema, estado, observaciones))
            self.connection.commit()
            print("Tiquet agregado exitosamente.")

        except cx_Oracle.Error as error:
            print("Error al agregar el Tiquet:", error)

    def eliminar_tiquet(self, id_tiquet):#FUNCIONA BIEN
        try:
            self.cursor.execute("DELETE FROM Tiquet WHERE ID_Tiquet = :1", (id_tiquet,))
            self.connection.commit()
            print(f"Tiquet con ID {id_tiquet} eliminado exitosamente.")

        except cx_Oracle.Error as error:
            print(f"Error al eliminar el Tiquet con ID {id_tiquet}:", error)

    #FUNCIONA BIEN
    def editar_tiquet(self, id_tiquet, id_nuevo_usuario_creador, id_nuevo_usuario_asignado, id_nuevo_cliente_asignado, id_nuevo_tipo_tiquet, id_nuevo_criticidad, id_nuevo_area_destino, detalles_servicio, detalles_problema, estado, observaciones):
        try:
            self.cursor.execute("""
                UPDATE Tiquet
                SET ID_UsuarioCreador = :1,
                    ID_UsuarioAsignado = :2,
                    ID_ClienteAsignado = :3,
                    ID_TipoTiquet = :4,
                    ID_Criticidad = :5,
                    ID_AreaDestino = :6,
                    DetalleServicio = :7,
                    DetalleProblema = :8,
                    Estado = :9,
                    Observacion = :10
                WHERE ID_Tiquet = :11
            """, (id_nuevo_usuario_creador, id_nuevo_usuario_asignado, id_nuevo_cliente_asignado, id_nuevo_tipo_tiquet, id_nuevo_criticidad, id_nuevo_area_destino, detalles_servicio, detalles_problema, estado, observaciones, id_tiquet))
            self.connection.commit()
            print(f"El Tiquet con ID {id_tiquet} se actualizó exitosamente.")
        except cx_Oracle.Error as error:
            print(f"Error al editar el Tiquet con ID {id_tiquet}: {error}")
