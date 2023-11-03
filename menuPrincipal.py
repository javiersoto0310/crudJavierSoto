from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys
import os

class Ventana_menu(QMainWindow):
    def menu_opciones(self):
            #contenedor de menú de opciones
            self.setWindowTitle("Programa de administración datos")
            self.setFixedSize(1360, 800)
            self.setStyleSheet("background: white")

            #Contenedor del título.
            self.fr_titulo = QFrame(self)
            self.fr_titulo.setGeometry(10, 10, 1330, 100)
            self.fr_titulo.setStyleSheet("background: grey")

            #Texto del título.
            self.titulo = QLabel(self.fr_titulo)
            self.titulo.setText("Menú principal")
            self.titulo.setGeometry(0, 20, 1330, 60)
            self.titulo.setAlignment(Qt.AlignCenter)
            self.titulo.setStyleSheet('''
                                    color: black;
                                    font-size: 40px
                                  ''')
           # contenedor Botón.
            self.frame = QFrame(self)
            self.frame.setGeometry(10, 130, 1330, 540)
            self.frame.setStyleSheet("background: grey")

            #Botón registrar empleado.
            self.boton_registrar = QPushButton(self.frame)
            self.boton_registrar.setText("Registrar empleado")
            self.boton_registrar.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
            self.boton_registrar.setGeometry(163, 50, 440, 50)
          
            #Botón consultar datos del empleado.
            self.boton_consultar_empleado = QPushButton(self.frame)
            self.boton_consultar_empleado.setText("Consultar datos empleados")
            self.boton_consultar_empleado.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
            self.boton_consultar_empleado.setGeometry(700, 50, 440, 50)

            #Botón registrar cliente.
            self.boton_registrar_cliente = QPushButton(self.frame)
            self.boton_registrar_cliente.setText("Registrar cliente")
            self.boton_registrar_cliente.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
            self.boton_registrar_cliente.setGeometry(163, 150, 440, 50)
          
            #Botón consultar datos del cliente.
            self.boton_consultar_cliente = QPushButton(self.frame)
            self.boton_consultar_cliente.setText("Consultar datos cliente")
            self.boton_consultar_cliente.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
            self.boton_consultar_cliente.setGeometry(700, 150, 440, 50)

             #Botón registrar proveedor.
            self.boton_registrar_cliente = QPushButton(self.frame)
            self.boton_registrar_cliente.setText("Registrar proveedor")
            self.boton_registrar_cliente.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
            self.boton_registrar_cliente.setGeometry(163, 250, 440, 50)
          
            #Botón consultar datos del cliente.
            self.boton_consultar_proveedor = QPushButton(self.frame)
            self.boton_consultar_proveedor.setText("Consultar datos proveedor")
            self.boton_consultar_proveedor.setStyleSheet('''
                                    color: white;
                                    font-size: 25px;
                                  ''')
            self.boton_consultar_proveedor.setGeometry(700, 250, 440, 50)
           
           