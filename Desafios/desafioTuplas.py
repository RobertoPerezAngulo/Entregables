# Desafio de tuplas
# Autor: Jose Roberto Perez Angulo
# Fecha: 30/06/2023

tupla = (8,15,4,39,5,89,87,19,7,-755,88,123,2,11,15,9,355)
print('El contenido de la tupla es: ', tupla)


ultimoItemTupla = tupla[-1]

# Imprimir el primer item de la tupla
print('El ultimo item de la tupla es: ', ultimoItemTupla)
print('Numero de items de tupla: ', len(tupla))
print('Donde se encuntra el numero: ', tupla.index(87))

# Lita de los tres ultimos numeros  
print('Los tres ultimos numeros de la tupla son: ', tupla[-3:])


# un itam que hya eb la posicion 8 de tupla
print('El item que hay en la posicion 8 de la tupla es: ', tupla[8])

# numero de veces que el item 7 aparece en la tupla
print('El numero de veces que el item 7 aparece en la tupla es: ', tupla.count(7))