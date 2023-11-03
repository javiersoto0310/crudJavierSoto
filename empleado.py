from persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, dni):
        super().__init__(nombre, apellido, edad)
        self.dni = int(dni)

    def info_pedida(self):
        datos_persona = super().info_pedida_principal()
        return datos_persona, self.dni 
        