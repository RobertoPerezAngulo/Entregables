# Expresiones enidadas
# Autor: Jose Roberto Perez Angulo
# Fecha: 05/07/2023


litas_numeros = [1,2,3,4,5]

# Imprimir el contenido de la lista
print('El contenido de la lista es: ', litas_numeros)
invertir_lista = litas_numeros[0][::-1]
print('El contenido de la lista invertida es: ', invertir_lista)

nombre = input('¿Cual es tu nombre?:  ')

#condiciones
if not nombre.find('****') == -1:
    print('El nombre no puede ser', nombre)
    exit();
else:
    print('Bienvenido ', nombre)


