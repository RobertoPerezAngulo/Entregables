# Autor: Jose Roberto Pérez Angulo
# Fecha: 28/07/2023
# Descripción: Utilizar una funcion para almacenar dicha información, con el para usuario-contrasenia
# Utilizar un diccionario para almacenar dicha informacion con el par Usuario-contrasenia
# Utilizar otra funcion para login de usuarios, comprobando que la contraseia coicida con el usuario
import os


# Crear un archivo txt para almacenar la informacion
def crearArchivo():
    file = open("data.txt", "w")
    file.write("[]")
    file.close()

# Leer archivo txt
def leerArchivo():
    file = open("data.txt", "r")
    data = file.read()
    file.close()
    #print(data)
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

#Login de usuario
def login():
    try:
        # Valida si existe el archivo
        if existeArchivo() == False:
            crearArchivo()
        # Lee el archivo
        data = eval(leerArchivo())
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        for i in data:
            if i["user"] == user and i["password"] == password:
                print("Bienvenido " + i["nombre"])
                break
            else:
                print("Usuario o contraseña incorrectos")
        else:
            print("No existe datos favor de crear el archivo")
    except Exception as e:
        print("Error al almacenar la informacion " +  e.__str__() )




# Funcion para validar el usuario
select = input('Seleccione una opcion: \n 1. Almacenar informacion \n 2. Login \n 3. Salir \n')
if(select == "1"):
    almacenarInformacion()
elif(select == "2"):
    login()
elif(select == "3"):
    exit()
