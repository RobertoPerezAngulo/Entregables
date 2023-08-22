class Person():
    def __init__(self,name,lastName):
        self.__name = name
        self.__lastName = lastName

class Rol():
    def __init__(self,rol):
        self.__rol = rol

class User(Person, Rol):
    def __init__(self, name, lastName, username, password, rol):
        super().__init__(name, lastName)
        Rol.__init__(self,rol)
        self.__username = username
        self.__password = password


userAll = []


def addUser():
    name = input("Ingrese el nombre del usuario: ")
    lastName = input("Ingrese el apellido del usuario: ")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    rol = input("Ingrese el rol del usuario: ")
    user = User(name, lastName, username, password, rol)
    userAll.append(user)
    return user



def showUser():
    for i in userAll:
        # Imprime el nombre y apellido del usuario
        print(i._Person__name, i._Person__lastName)

addUser()
showUser()     