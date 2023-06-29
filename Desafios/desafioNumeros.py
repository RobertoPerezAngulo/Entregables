# calculo promedio de partidos ganados, perdidos y empatados
# Autor: Jose Roberto Perez Angulo
# Fecha: 29/06/2023

# Declaracion de variables
partidos_ganados = input('¿Cuantos partidos ganados tiene el equipo?:  ')
partidos_perdidos = input('¿Cuantos partidos perdidos tiene el equipo?:  ')
partidos_empatados = input('¿Cuantos partidos empatados tiene el equipo?:  ')

# Reglas de juego
if(int(partidos_ganados) +  int(partidos_perdidos) + int(partidos_empatados) > 20):
    print('El numero de partidos no puede ser mayor a 20')
    exit()

# Calculo de puntos
partidos_ganados= int(partidos_ganados) * 3
partidos_perdidos= int(partidos_perdidos) * 0
partidos_empatados= int(partidos_empatados) * 1

# Calculo de promedio
promedio = (int(partidos_ganados) + int(partidos_perdidos) + int(partidos_empatados)) / 3

# Imprimir resultado
print('El promedio de puntos del equipo es: ', promedio)