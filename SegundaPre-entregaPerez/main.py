#Crear un programa que permita el modelamiento de clientes en un pagina de compras. Se debe utilizar el concepto de programacion orientada o objectos


class Person():
    def __init__(self, id, name, age, lastaname, address, phone):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__lastaname = lastaname
        self.__address = address
        self.__phone = phone

    def getNamePerson(self):
        return f"Hi, sr. {self.__name} {self.__lastaname}"
    
    def __str__(self):
        return f"all data: ID -> {self.__id} NAME -> {self.__name} AGE ->{self.__age} LASTNAME ->{self.__lastaname} ADDRESS ->{self.__address} PHONE ->{self.__phone}"

class client(Person):
    def __init__(self, id, name, age, lastaname, address, phone,user,password):
        super().__init__(id, name, age, lastaname, address, phone)
        self.__user = user
        self.__password = password
        self.__family = []
        self.__shopping_cart = []

    def getLogin(self):
        return f"Hi, sr. {self.getNamePerson()} your user is {self.__user} and your password is {self.__password}"
    
    def getFamily(self):
        family_info = ""
        for member in self.__family:
            family_info += f"{member['name']} ({member['relation']}), "
        return f"Family members: {family_info} shoting cart: {self.getShoppingCart()}"
    
    def getShoppingCart(self):
        shopping = ""
        for item in self.__shopping_cart:
            shopping += f"{item['name']} ({item['price']}),"
        return f"Shopping cart: {shopping}"

    def getAllData(self):
        return str(self)

cliente = client(1, "Juan", 30, "Perez", "Calle A", "123456", "juancito", "clave123")
cliente._client__family.append({"name": "María", "relation": "esposa"})
cliente._client__family.append({"name": "Pedro", "relation": "hijo"})
cliente._client__family.append({"name": "Marta", "relation": "hija"})
cliente._client__shopping_cart.append({"name": "TV", "price": 1000})
cliente._client__shopping_cart.append({"name": "Laptop", "price": 2000})
cliente._client__shopping_cart.append({"name": "Celular", "price": 3000})


print(cliente.getLogin())
print(cliente.getFamily())
print(cliente.getAllData())