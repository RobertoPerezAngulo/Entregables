#Ecribir in algoritmo que pida al usuario que ingrese un mensaje e imprimir por pantalla la cantidad de palabras que compone ese mensaje.
# Autor: Jose Roberto Perez Angulo
# Fecha: 29/06/2023
#



# Declaracion de variables
mesanje = input('Ingrese un mensaje: ')
lista = mesanje.split()

# Imprimir resultado
print('El contenido de la lista es: ', lista)
print('La cantidad de palabras que componen el mensaje es: ', len(lista))



