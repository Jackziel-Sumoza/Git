# creamos un objeto que contiene el metodo presentar, para presentar a una persona registrada en una base de datos
class PersonaNatural():
    def __init__(self,nombre_usuario,apellido_usuario,profesion):
        self.nombre = nombre_usuario
        self.apellido = apellido_usuario
        self.profesion = profesion
        
    def presentar(self):
        return f"¡Hola! mi nombre es {self.nombre} {self.apellido} y soy {self.profesion}"

jackziel_sumoza = PersonaNatural("Jackziel","Sumoza","Programador Web")

print(jackziel_sumoza.presentar())