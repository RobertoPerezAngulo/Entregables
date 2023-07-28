import json

documento = "./Tareas/cuidades.json"

def readDocument():
    file = open(documento,'r')
    data = json.load(file)
    file.close()
    return data

dataCuidad = readDocument()
dataCuidad = dataCuidad["cuidad"]


def welcomeCity(nombreCuidad):
    for ciudad in dataCuidad:
        if ciudad["nombre"] == nombreCuidad:
            print(f'Bienvenido a la cuidad de: {ciudad["nombre"]}') 
    else:
        print("No se encontro la cuidad...")





nombreCuidad = input("Ingrese el nombre de la cuidad: ")
welcomeCity(nombreCuidad)
