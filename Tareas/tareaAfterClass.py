#  Escribir un algoritmo que pida al usuario que ingrese un mensaje e imprima por pantalla la cantidad de palabras que se compone el mensaje
mensaje = input('Ingrese un mensaje: ')
palabras = mensaje.split() 
print('El mensaje tiene', len(palabras), 'palabras')
