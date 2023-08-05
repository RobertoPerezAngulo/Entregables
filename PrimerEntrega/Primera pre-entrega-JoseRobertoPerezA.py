# Autor: Jose Roberto Pérez Angulo
# Fecha: 28/07/2023
# Descripción: Utilizar una funcion para almacenar dicha información, con el para usuario-contrasenia
# Utilizar un diccionario para almacenar dicha informacion con el par Usuario-contrasenia
# Utilizar otra funcion para login de usuarios, comprobando que la contraseia coicida con el usuario

#Se realizan observaciones
#En primer lugar, el programa que hiciste es más complejo de lo necesario. Si bien se nota que intentaste darle funcionalidades muy interesantes, terminaste por enredarte en algunas cosas que lo hacen funcionar mal.
#Otro tema en general es que la estructura try-except no se debe utilizar para encerrar grandes porciones de código porque que gasta más recursos del sistema. Try-except es solo para capturar excepciones en la parte de un código que no es controlada por el programa, como cuando un usuario ingresa datos o cuando intentamos leer un archivo con open('archivo', 'r').
#En la función login() utilizaste un ciclo for-else. Este tipo de estructura no la vimos en la clase porque es muy poco común, pero lo que hace es ejecutar lo que haya escrito en else: después de terminar el ciclo. Por cómo lo usaste, esta función imprime el mensaje "Usuario o contraseña incorrectos" y devuelve False aún cuando el usuario y contraseña eran correctos.
#En la función accesoAdminImprimeUsuarios() la variable data solo se asigna cuando el login() devuelve un True, pero si el login() devuelve False esa variable no existe y la función se sigue ejecutando, entonces al llegar al ciclo for e intentar leer esa variable, el programa se rompe.

import os

data = [{
    "id": 1,
    "nombre": "Administrador",
    "user": "admin",
    "password": "123",
    "role": 1
}]



# Crear un archivo txt para almacenar la informacion
def crearArchivo():
    try:
        file = open("data.txt", "w")
        file.write(str(data))
        file.close()
    except Exception as e:
        print("Error al crear el archivo " +  e.__str__() )

# Leer archivo txt
def leerArchivo():
    try:
        file = open("data.txt", "r")
        data = eval(file.read())
        file.close()
        return data
    except Exception as e:
        print("Error al leer el archivo " +  e.__str__() )
    

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
        if not existeArchivo():
            crearArchivo()
        # Lee el archivo
        data = leerArchivo()
        #Obtenemos el ultimo numero digitado
        id = int(len(data)) + 1 
        nombre = input("Ingrese su nombre: ")
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
        role = registraRol()
        data.append({"id": id, "nombre": nombre, "user": user, "password": password, "role": role})
        guardarInformacion(data)
    except Exception as e:
        print(e.__str__() )

# Guarda la informacion en el txt
def guardarInformacion(data):
    try:
        file = open("data.txt", "w")
        file.write(str(data))
        file.close()
        print("Informacion guardada con exito")
    except Exception as e:
        print("Error al guardar la informacion " +  e.__str__() )

# Funcion para validar el usuario
def  registraRol():
    rol = int(input("selecciona un rol: \n 1. Administrador \n 2. Usuario\n op: "))
    if(rol > 0 and rol < 3):
        return rol
    return registraRol()

#Login de usuario
def login():
    if(not existeArchivo()):
        crearArchivo()
    # Lee el archivo
    data = leerArchivo()
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    for i in data:
        if i["user"] == user and i["password"] == password:
            print("Bienvenido usuario " + i["nombre"].upper() + " al sistema")
            return int(i.get("role"))
        if data.index(i) == len(data) - 1:
            print("Usuario o contraseña incorrectos")
            exit()
        

# Imprime los usuarios
def accesoAdminImprimeUsuarios():
    data = leerArchivo()
    for i in data:
        print("Nombre: " + i["nombre"].upper() + " Usuario: " + i["user"] + " Contraseña: " + i["password"])
    

# Funcion para validar el usuario e ingresar al sistema
def accesoUsuario():
    print("Bienvenido al sistema")
    print("El usuario administrador es usuario: admin  passsword: 123")
    role = login()
    if(role == 1):
        select = input('Seleccione una opcion: \n 1. Crear usuario \n 2. Imprime usuarios \n 3. Salir \n op: ')
        if(select == "1"):
            almacenarInformacion()
        elif(select == "2"):
            accesoAdminImprimeUsuarios()
        elif(select == "3"):
            exit()
        else:
            print("Opcion no valida")
    elif(role == 2):
        select = input('Seleccione una opcion: \n 1. Crear usuario  \n 2. Salir \n op: ')
        if(select == "1"):
            almacenarInformacion()
        elif(select == "2"):
            exit()
        else:
            print("Opcion no valida")



accesoUsuario()