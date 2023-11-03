
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from menuPrincipal import Ventana_menu
from ventanaRegistrar import VentanaRegistrar
from datosEmpleados import ConsultarModificarEliminarEmpleado

class Aplicacion:
    def __init__(self):
        self.menu = Ventana_menu()
        self.registrar = VentanaRegistrar()
        self.consultarModificarEliminarEmpleado = ConsultarModificarEliminarEmpleado()
        
        self.menu.menu_opciones()
        self.registrar.pantalla()
        self.consultarModificarEliminarEmpleado.cmeEmpleado()
        
        self.menu.boton_registrar.clicked.connect(self.abrir_pantalla_registro)
        self.registrar.boton_volver_al_menu.clicked.connect(self.volver_registrar_a_menu_principal)
        self.menu.boton_consultar_empleado.clicked.connect(self.ir_de_menu_a_pantalla_consultar_modificar_eliminar_empleado)
        self.consultarModificarEliminarEmpleado.boton_volver.clicked.connect(self.volver_pantalla_cmeempleado_a_menu)
        
    def abrir_pantalla_registro(self):
        self.menu.hide()
        self.registrar.show() 

    def volver_registrar_a_menu_principal(self):
        self.registrar.hide()
        self.menu.show()      
    
    def ir_de_menu_a_pantalla_consultar_modificar_eliminar_empleado(self):
        self.menu.hide()
        self.consultarModificarEliminarEmpleado.show()
       

    def volver_pantalla_cmeempleado_a_menu(self):
        self.consultarModificarEliminarEmpleado.hide()
        self.menu.show()
      
import sys
ap = QApplication(sys.argv) 
main = Aplicacion()
main.menu.show()
sys.exit(ap.exec_())