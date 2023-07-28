import cx_Oracle

class Conexion: 

    def __init__(self):


        self.__connection = cx_Oracle.connect(user="gustavo", password=".Inacap2023.", dsn="dbtaller_high")

        self.__cursor = self.__connection.cursor()

    def getConexion(self):

        return self.__connection

    def getCursor(self):

        return self.__cursor

    def cerrarConexion(self):

        self.__cursor.close()

        self.__connection.close()
