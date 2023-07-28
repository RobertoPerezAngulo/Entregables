# Autor: Jose Roberto Pérez Angulo
# Fecha: 17/09/2021
# Descripción: Utilizar una funcion para almacenar dicha información, con el para usuario-contrasenia
# Utilizar un diccionario para almacenar dicha informacion con el par Usuario-contrasenia
# Utilizar otra funcion para login de usuarios, comprobando que la contraseia coicida con el usuario
import json
import os

data = [{
    "id": "1",
    "nombre" : "Admin",
    "user" : "",
    "password" : ""
}]

# Crear un archivo txt para almacenar la informacion
def crearArchivo():
    file = open("data.txt", "w")
    file.write(str(data))
    file.close()

# Leer archivo txt
def leerArchivo():
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    print(data)
    return data

# Identifica si existe el txt
def existeArchivo():
    if os.path.isfile("data.txt"):
        return True
    else:
        return False


# Funcion para almacenar la informacion
def almacenarInformacion():
    try:
        # Valida si existe el archivo
        if existeArchivo() == False:
            crearArchivo()
        # Lee el archivo
        data = eval(leerArchivo())
        id = int(len(data)) + 1 
        nombre = input("Ingrese su nombre: ")
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        data.append({"id": id, "nombre": nombre, "user": user, "password": password})
        guardarInformacion(data)
    except Exception as e:
        print("Error al almacenar la informacion " +  e.__str__() )

# Escribe en la funcion 
def guardarInformacion(data):
    file = open("data.txt", "w")
    file.write(str(data))
    file.close()
    print("Informacion guardada con exito")


# Funcion para validar el usuario
almacenarInformacion()