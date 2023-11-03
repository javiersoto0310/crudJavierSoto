
class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = str(nombre)
        self.apellido =str(apellido)
        self.edad = int(edad)

    def info_pedida_principal(self):
        return self.nombre, self.apellido, self.edad     
    
    