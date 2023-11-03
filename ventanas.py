from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
import os

class Ventana:
    def ventanaRegistrar(self):
     
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
             