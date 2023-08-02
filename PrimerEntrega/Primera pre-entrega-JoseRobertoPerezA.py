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
                print("Bienvenido usuario " + i["nombre"].upper() + " al sistema")
                #Es usuario administrador
                if(i.get('user') == "admin" and i.get('password') == "123"):
                    return True
        else:
            print("Usuario o contraseña incorrectos")
            return False
    except Exception as e:
        print("Error al almacenar la informacion " +  e.__str__() )

# Imprime la informacion
def accesoAdminImprimeUsuarios():
    if(login() == True):
        data = eval(leerArchivo())
    else:
        print("No tiene permisos para acceder a la informacion")
        exit()
    for i in data:
        print("\nLa información es confidencial, solo el administrador puede acceder a la información")
        print(f"El {i.get('id')} es Nombre es {i.get('nombre').upper()} " +  
              f"y el acceso al sistema es {i.get('user').upper()} " +
              f"con un password {i.get('password').upper()}")



# Funcion para validar el usuario
select = input('Seleccione una opcion: \n 1. Almacenar informacion \n 2. Login \n 3. Imprime usuarios \n 4. Salir \n op: ')
if(select == "1"):
    almacenarInformacion()
elif(select == "2"):
    login()
elif(select == "3"):
    accesoAdminImprimeUsuarios()
elif(select == "4"):
    exit()
else:
    print("Opcion no valida")
