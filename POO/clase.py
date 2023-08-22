class Persona():
    def __init__(self,nombre,apellidoPaterno,apellidoMaterno):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
    def getNombre(self):
        return self.nombre
    def getApellidoPaterno(self):
        return self.apellidoPaterno 
    def getApellidoMaterno(self):
        return self.apellidoMaterno
    def setNombre(self,nombre):
        self.nombre = nombre

#Imprime valores
def imprimeValores():
    persona = Persona("Jose","Perez","Aguilar")
    print("Nombre: " + persona.getNombre() + " Apellido Paterno: " + persona.getApellidoPaterno() + " Apellido Materno: " + persona.getApellidoMaterno())


imprimeValores()