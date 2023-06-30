# Notas final de estudiantes
# Autor: Jose Roberto Perez Angulo
# Fecha: 29/06/2023

# Declaracion de variables
nota_1 = input('¿Cual es la nota del primer parcial?:  ')
nota_2 = input('¿Cual es la nota del segundo parcial?:  ')
nota_3 = int(input('¿Cual es la nota del tercer parcial?:  '))

# Reglas de juego
promedio = (int(nota_1) + int(nota_2) + int(nota_3)) / 3

# Imprimir resultado
print('El promedio es: ', promedio)