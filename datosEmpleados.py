from PySide6.QtWidgets import *
from PySide6.QtCore import *
import mysql.connector 
from conexionMYSQL import *
import sys
import os

class ConsultarModificarEliminarEmpleado(QMainWindow):
    
    def cmeEmpleado(self):
        
        #Contenedor principal
        self.setWindowTitle("Programa de administración datos")
        self.setFixedSize(1360, 800)
        self.setStyleSheet("background: white")
       
        #Contenedor de la tabla.
        self.frame_tabla = QFrame(self)
        self.frame_tabla.setGeometry(700, 30, 600, 630)
        self.frame_tabla.setStyleSheet("background: grey")
        self.titulo = QLabel(self.frame_tabla)
        self.titulo.setText(" "* 24 +"Base de datos empleados")
        self.titulo.setStyleSheet('''
                                    color: black;
                                    font-size: 25px;
                                  ''')
       
        #Contenedor del inputs.
        self.frame_inputs = QFrame(self)
        self.frame_inputs.setGeometry(50, 30, 600, 630)
        self.frame_inputs.setStyleSheet("background: grey")
        self.titulo = QLabel(self.frame_inputs)
        self.titulo.setText(" "* 13 +"Consultar Modificar Eliminar Empleado")
        self.titulo.setStyleSheet('''
                                    color: black;
                                    font-size: 25px;
                                  ''')
        
        self.frame_nota = QFrame(self.frame_inputs)
        self.frame_nota.setGeometry(20,480 ,570,150)
        self.frame_nota.setStyleSheet("background: grey")
        self.nota= QLabel(self.frame_nota)
        self.nota.setText(""" Nota: * Para modificar los datos del empleado es obligación completar 
             todos los campos. Luego presionar "Modificar".
                          
           * Para eliminar todos los datos del empleado solo debe ingresar
             el número de ID. Luego presionar "Eliminar".""")
        self.nota.setStyleSheet('''
                                    color: black;
                                    font-size: 17px;
                                  ''')

        #Input id consultar
        self.input_id = QLineEdit(self.frame_inputs)
        self.input_id.setGeometry(20, 50 ,100, 30)
        self.input_id.setPlaceholderText("id")
        self.input_id.setStyleSheet("background: white; color: black;font-size: 15px")

        #Botón consultar por id.
        self.boton_consultar_por_id = QPushButton(self.frame_inputs)
        self.boton_consultar_por_id.setText("Consultar")
        self.boton_consultar_por_id.setStyleSheet('''
                                    color: white;
                                    font-size: 20px
                                  ''')
        self.boton_consultar_por_id.setGeometry(20,100,100,30)
        self.boton_consultar_por_id.clicked.connect(self.buscar_por_id)
        self.input_id.returnPressed.connect(self.boton_consultar_por_id.click)

        #Input nombre
        self.input_nombre = QLineEdit(self.frame_inputs)
        self.input_nombre.setGeometry(140, 50 ,100, 30)
        self.input_nombre.setPlaceholderText("Nombre")
        self.input_nombre.setStyleSheet("background: white; color: black;font-size: 15px")

        #Botón consultar por nombre.
        self.boton_consultar_por_nombre = QPushButton(self.frame_inputs)
        self.boton_consultar_por_nombre.setText("Filtrar")
        self.boton_consultar_por_nombre.setStyleSheet('''
                                    color: white;
                                    font-size: 15px
                                  ''')
        self.boton_consultar_por_nombre.setGeometry(140,100,100,30)
        self.boton_consultar_por_nombre.clicked.connect(self.buscar_por_nombre)
        self.input_id.returnPressed.connect(self.boton_consultar_por_nombre.click)

        #Input apellido
        self.input_apellido = QLineEdit(self.frame_inputs)
        self.input_apellido.setGeometry(260, 50 ,100, 30)
        self.input_apellido.setPlaceholderText("Apellido")
        self.input_apellido.setStyleSheet("background: white; color: black;font-size: 15px")
  
        #Botón consultar por apellido.
        self.boton_consultar_por_apellido = QPushButton(self.frame_inputs)
        self.boton_consultar_por_apellido.setText("Filtrar")
        self.boton_consultar_por_apellido.setStyleSheet('''
                                    color: white;
                                    font-size: 15px
                                  ''')
        self.boton_consultar_por_apellido.setGeometry(260,100,100,30)
        self.boton_consultar_por_apellido.clicked.connect(self.buscar_por_apellido)
        self.input_id.returnPressed.connect(self.boton_consultar_por_apellido.click)

        #Input edad
        self.input_edad = QLineEdit(self.frame_inputs)
        self.input_edad.setGeometry(380, 50 ,100, 30)
        self.input_edad.setPlaceholderText("Edad")
        self.input_edad.setStyleSheet("background: white; color: black;font-size: 15px")

         #Botón consultar por edad.
        self.boton_consultar_por_edad = QPushButton(self.frame_inputs)
        self.boton_consultar_por_edad.setText("Filtrar")
        self.boton_consultar_por_edad.setStyleSheet('''
                                    color: white;
                                    font-size: 15px
                                  ''')
        self.boton_consultar_por_edad.setGeometry(380,100,100,30)
        self.boton_consultar_por_edad.clicked.connect(self.buscar_por_edad)
        self.input_id.returnPressed.connect(self.boton_consultar_por_edad.click)

        #Input dni
        self.input_dni = QLineEdit(self.frame_inputs)
        self.input_dni.setGeometry(490,50,100,30)
        self.input_dni.setPlaceholderText("dni")
        self.input_dni.setStyleSheet("background: white; color: black;font-size: 15px")

        #Botón consultar por dni.
        self.boton_consultar_por_dni = QPushButton(self.frame_inputs)
        self.boton_consultar_por_dni.setText("Filtrar")
        self.boton_consultar_por_dni.setStyleSheet('''
                                    color: white;
                                    font-size: 15px
                                  ''')
        self.boton_consultar_por_dni.setGeometry(490, 100, 100, 30)
        self.boton_consultar_por_dni.clicked.connect(self.buscar_por_dni)
        self.input_id.returnPressed.connect(self.boton_consultar_por_dni.click)

        #Botón modificar.
        self.boton_modificar_registro_empleado = QPushButton(self.frame_inputs)
        self.boton_modificar_registro_empleado.setText("Modificar")
        self.boton_modificar_registro_empleado.setStyleSheet('''
                                    color: green;
                                    font-size: 20px
                                  ''')
        self.boton_modificar_registro_empleado.setGeometry(20, 180, 100, 30)
        self.boton_modificar_registro_empleado.clicked.connect(self.datos_modificar)
        self.input_id.returnPressed.connect(self.boton_modificar_registro_empleado.click)

        #Botón eliminar.
        self.boton_eliminar_datos_empleados = QPushButton(self.frame_inputs)
        self.boton_eliminar_datos_empleados.setText("Eliminar")
        self.boton_eliminar_datos_empleados.setStyleSheet('''
                                    color: red;
                                    font-size: 20px
                                  ''')
        self.boton_eliminar_datos_empleados.setGeometry(20, 250, 100, 30)
        self.boton_eliminar_datos_empleados.clicked.connect(self.eliminar_datos_empleado)
        self.input_id.returnPressed.connect(self.boton_eliminar_datos_empleados.click)

       #Botón listar todos los empleados.
        self.boton_consulta_general = QPushButton(self.frame_inputs)
        self.boton_consulta_general.setText("Listar todos los empleados")
        self.boton_consulta_general.setStyleSheet('''
                                    color: white;
                                    font-size: 20px
                                  ''')
        self.boton_consulta_general.setGeometry(140, 180, 450, 30)
        self.boton_consulta_general.clicked.connect(self.listar_todos_los_empleados)
        self.input_id.returnPressed.connect(self.boton_consulta_general.click)

         #Botón volver.
        self.boton_volver = QPushButton(self.frame_inputs)
        self.boton_volver.setText("Volver al menú")
        self.boton_volver.setStyleSheet('''
                                    color: white;
                                    font-size: 20px
                                  ''')
        self.boton_volver.setGeometry(140, 250, 450, 30)
    
    def buscar_por_id(self):
        texto_id = self.input_id.text()
        texto_id = (texto_id)
        empleados = Conexion.conectarBbdd()
        
        mycursor = empleados.cursor()
        consulta = "SELECT * FROM datos_personales WHERE id ='{}'".format(texto_id)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
    
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item) 

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.input_id.clear()
        self.tabla.show()   
        
    def buscar_por_dni(self):
        texto_dni = self.input_dni.text()
        texto_dni = (texto_dni)
        empleados = Conexion.conectarBbdd()
        
        mycursor = empleados.cursor()
        consulta = "SELECT * FROM datos_personales WHERE dni = '{}'".format(texto_dni)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
       
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.input_dni.clear()
        self.tabla.show()

    def buscar_por_nombre(self):
       
        texto_nombre = self.input_nombre.text()
        texto_nombre = (texto_nombre)
        empleados = Conexion.conectarBbdd() 

        mycursor = empleados.cursor()
        consulta = "SELECT * FROM datos_personales WHERE nombre = '{}'".format(texto_nombre)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
        
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.input_nombre.clear()
        self.tabla.show()
          
    def buscar_por_apellido(self):
        texto_apellido = self.input_apellido.text()
        texto_apellido = (texto_apellido)
        empleados = Conexion.conectarBbdd()

        mycursor = empleados.cursor()
        consulta = "SELECT * FROM datos_personales WHERE apellido ='{}'".format(texto_apellido)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
       
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.input_apellido.clear()
        self.tabla.show()

    def buscar_por_edad(self):
        texto_edad = self.input_edad.text()
        texto_edad = (texto_edad)
        empleados = Conexion.conectarBbdd() 

        mycursor = empleados.cursor()
        consulta = "SELECT * FROM datos_personales WHERE edad ='{}'".format(texto_edad)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
       
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.input_edad.clear()
        self.tabla.show()  

    def listar_todos_los_empleados(self):
        empleados = Conexion.conectarBbdd()

        mycursor = empleados.cursor()
        consulta = ("SELECT * FROM datos_personales;")
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
       
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.tabla.show()     

    def datos_modificar(self):
        texto_nombre = self.input_nombre.text()
        texto_apellido = self.input_apellido.text()
        texto_edad = self.input_edad.text()
        texto_dni = self.input_dni.text()
        texto_id = self.input_id.text()
        
        texto_nombre = str(texto_nombre)
        texto_apellido = str(texto_apellido)
        texto_edad = (texto_edad)
        texto_dni = (texto_dni)
        texto_id = (texto_id)

        self.input_nombre.clear()
        self.input_apellido.clear()
        self.input_edad.clear()
        self.input_dni.clear()
        self.input_id.clear()

        empleados = Conexion.conectarBbdd()

        mycursor = empleados.cursor()
        consulta ="UPDATE datos_personales SET nombre = '{}', apellido ='{}', edad ='{}',dni = '{}' WHERE id = '{}'".format(texto_nombre, texto_apellido, texto_edad, texto_dni, texto_id)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()

        mycursor = empleados.cursor()
        consulta ="SELECT * FROM datos_personales WHERE id ='{}'".format(texto_id)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
       
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.tabla.show()     

    def eliminar_datos_empleado(self):
        texto_id = self.input_id.text()
        texto_id = (texto_id)
        self.input_id.clear()
        empleados = Conexion.conectarBbdd() 

        mycursor = empleados.cursor()
        consulta = "DELETE FROM datos_personales WHERE id = '{}'".format(texto_id)
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()

        mycursor = empleados.cursor()
        consulta = ("SELECT * FROM datos_personales;")
        mycursor.execute(consulta)
        datos_empleados = mycursor.fetchall()
        empleados.commit()
       
        self.tabla = QTableWidget(self.frame_tabla)
        self.tabla.setGeometry(40, 50, 600, 560)
        self.tabla.setRowCount(len(datos_empleados))
        self.tabla.setColumnCount(len(datos_empleados[0]))
        self.tabla.setHorizontalHeaderLabels(["Id","Nombre", "Apellido", "Edad", "Dni"])

        for fila, datos_fila in enumerate(datos_empleados):
            for columna, valor in enumerate(datos_fila):
                item = QTableWidgetItem(str(valor))
                self.tabla.setItem(fila,columna,item)


        self.dialogo = QDialog(self)
        self.dialogo.setWindowTitle("Programa de administración de datos.")
        self.dialogo.setGeometry(460,300,400, 200)
        self.dialogo.setStyleSheet("background: grey")
  
        self.titulo_dilogo =  QFrame(self.dialogo)
        self.cartel_ingreso_correcto = QLabel(self.dialogo)
        self.cartel_ingreso_correcto.setText("Datos del empleado eliminado!!!")
        self.cartel_ingreso_correcto.setGeometry(25,-60, 350, 300)
        self.cartel_ingreso_correcto.setAlignment(Qt.AlignCenter)
        self.cartel_ingreso_correcto.setStyleSheet('''
                                    color: green;
                                    font-size: 20px;
                                  ''')
        self.dialogo.show()        

        self.datos_tabla = QVBoxLayout()
        self.datos_tabla.addWidget(self.tabla)
        self.setLayout(self.datos_tabla)
        self.input_id.clear()
        self.tabla.show()

    def CrearTabla(self):
      self.tabla = QTableWidget()
      self.tabla.setRowCount()
      self.tabla.setColumnCount()
      self.datos_tabla = QVBoxLayout()
      self.datos_tabla.addWidget(self.tabla)
      self.setLayout(self.datos_tabla)  

   
