import mysql.connector

class Conexion:
    def conectarBbdd():
        try:
            empleados = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = "empleados"
                )
            print("Conectado") 
            return empleados 
        except mysql.connector.Error as error:
            print("Error de conexión {}".format(error))
            return empleados
         