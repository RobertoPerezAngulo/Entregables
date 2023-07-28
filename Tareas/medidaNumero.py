numeros = set()
suma = 0

def guardaNumero():
    while len(numeros) <= 2:
        agregaNumero = input("Ingresar un numero: ")
        numeros.add(agregaNumero)
    return numeros
    
datos = guardaNumero()
print(datos)

# for num in :
#     suma += int(num)

# suma = suma / len(numeros)
# print("El promedio es: ", suma)
