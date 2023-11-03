from PySide6.QtWidgets import *
from PySide6.QtCore import *
import mysql.connector
from conexionMYSQL import *
import datetime
import sys
import os

from empleado import Empleado

class VentanaRegistrar(QMainWindow):
    
    def __init__(self):
        super().__init__()
      #  self.pantalla()
 
    def pantalla(self):
        #Contenedor de registro de datos
        self.setWindowTitle("Programa de administración datos")
        self.setFixedSize(1350, 700)
        self.setStyleSheet("background: white")

        #Contenedor del título.
        self.fr_titulo = QFrame(self)
        self.fr_titulo.setGeometry(10, 10, 1330, 100)
        self.fr_titulo.setStyleSheet("background: grey")

        #Texto del título.
        self.titulo = QLabel(self.fr_titulo)
        self.titulo.setText("Ingresar datos")
        self.titulo.setGeometry(0, 20, 1330, 60)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setStyleSheet('''
                                    color: black;
                                    font-size: 40px;
                                  ''')

        #Contenedor de los inputs.
        self.frame_inputs = QFrame(self)
        self.frame_inputs.setGeometry(10, 130, 1330, 540)
        self.frame_inputs.setStyleSheet("background: grey")

        #Input.
        self.input_nombre = QLineEdit(self.frame_inputs)
        self.input_nombre.setGeometry(410, 30 ,460, 45)
        self.input_nombre.setPlaceholderText("Nombre")
        self.input_nombre.setStyleSheet("background: white; color: black;font-size: 20px")

        self.input_apellido = QLineEdit(self.frame_inputs)
        self.input_apellido.setGeometry(410, 110 ,460, 45)
        self.input_apellido.setPlaceholderText("Apellido")
        self.input_apellido.setStyleSheet("background: white; color: black;font-size: 20px")

        self.input_edad = QLineEdit(self.frame_inputs)
        self.input_edad.setGeometry(410, 190 ,460, 45)
        self.input_edad.setPlaceholderText("Edad")
        self.input_edad.setStyleSheet("background: white; color: black;font-size: 20px")
        
        self.input_dni = QLineEdit(self.frame_inputs)
        self.input_dni.setGeometry(410, 270 ,460, 45)
        self.input_dni.setPlaceholderText("Dni")
        self.input_dni.setStyleSheet("background: white; color: black;font-size: 20px")
        

        #Botón registrar.
        self.boton = QPushButton(self.frame_inputs)
        self.boton.setText("Registrar")
        self.boton.setStyleSheet('''
                                    color: black;
                                    font-size: 25px
                                  ''')
        self.boton.clicked.connect(self.crear_empleado)
        self.boton.setGeometry(410, 350, 460, 50)
        self.input_nombre.returnPressed.connect(self.boton.click)

       #Botón volver al menú.
        self.boton_volver_al_menu = QPushButton(self.frame_inputs)
        self.boton_volver_al_menu.setText("Regresar al menú principal.")
        self.boton_volver_al_menu.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
        self.boton_volver_al_menu.setGeometry(410, 430, 460, 50)
         
    def crear_empleado(self):
        texto_nombre = self.input_nombre.text()
        texto_apellido = self.input_apellido.text()
        texto_edad = self.input_edad.text()
        texto_dni = self.input_dni.text()
      
        try:
            texto_nombre = str(texto_nombre)
            texto_apellido = str(texto_apellido)
            texto_edad = int(texto_edad)
            texto_dni = int(texto_dni)

            empleado = Empleado(texto_nombre, texto_apellido, texto_edad, texto_dni)
            empleado.info_pedida()

            #crear base de datos
            empleados = Conexion.conectarBbdd()
            mycursor = empleados.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS  empleados")
            mycursor.execute("CREATE TABLE IF NOT EXISTS datos_personales (id INT PRIMARY KEY AUTO_INCREMENT,nombre VARCHAR(50), apellido VARCHAR(50), edad INT(3), dni INT(20))")

            sql = "INSERT INTO datos_personales (nombre, apellido, edad, dni) VALUES (%s, %s, %s,%s)"
            valores = (texto_nombre, texto_apellido, texto_edad,texto_dni)
            mycursor.execute(sql, valores)
            empleados.commit()

            #ventana secundaria, muestra los datos si están ingresados correctamente.
            self.dialogo = QDialog(self)
            self.dialogo.setWindowTitle("Datos cargados")
            self.dialogo.setGeometry(460,300,400, 200)
            self.dialogo.setStyleSheet("background: grey")
  
            self.titulo_dilogo =  QFrame(self.dialogo)
            self.cartel_ingreso_correcto = QLabel(self.dialogo)
            self.cartel_ingreso_correcto.setText("Empleado ingresado al sistema!!!")
            self.cartel_ingreso_correcto.setGeometry(25,-60, 350, 300)
            self.cartel_ingreso_correcto.setAlignment(Qt.AlignCenter)
            self.cartel_ingreso_correcto.setStyleSheet('''
                                    color: green;
                                    font-size: 20px;
                                  ''')
            self.dialogo.show()

            #creo archivo para guardar datos.
            #archivo = open("archivo.txt","a")
            #fecha_hora = datetime.datetime.now()
            #fecha_hora_final = fecha_hora.strftime("%d/%m/%Y %H:%M")
            #archivo.write(info_empleado + f"\nFECHA Y HORA: {fecha_hora_final}\n" + f"\n")
            #archivo.close()  

            self.input_nombre.clear()
            self.input_apellido.clear()
            self.input_edad.clear()
            self.input_dni.clear()

        except ValueError:
            #Ventana secundaria de cartel de datos mal imgresados.
            self.dialogo = QDialog(self)
            self.dialogo.setWindowTitle("Datos cargados")
            self.dialogo.setGeometry(460,300,400, 200)
            self.dialogo.setStyleSheet("background: grey")
  
            
            self.titulo_dilogo =  QFrame(self.dialogo)
            self.cartel_ingreso_incorrecto = QLabel(self.dialogo)
            self.cartel_ingreso_incorrecto.setText("Ha ingresado algún dato incorrecto!!!")
            self.cartel_ingreso_incorrecto.setGeometry(25,-60, 350, 300)
            self.cartel_ingreso_incorrecto.setAlignment(Qt.AlignCenter)
            self.cartel_ingreso_incorrecto.setStyleSheet('''
                                    color: red;
                                    font-size: 20px;
                                  ''')
            self.dialogo.show()
            
            self.input_nombre.clear()
            self.input_apellido.clear()
            self.input_edad.clear()
            self.input_dni.clear()
