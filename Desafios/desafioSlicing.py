# Desafio Slicing
# Autor: Jose Roberto Perez Angulo
# Fecha: 29/06/2023


# Declaracion de variables
cadena_original = "Jose Roberto Perez Angulo ha sacado una nota 5.8 en Materia matematicas"
cadena_volteada = cadena_original[::-1]


nombre_alumno=cadena_original[0:25]
calificacion=cadena_original[45:48]
materia=cadena_original[60:71]

# Imprimir resultado
print("Nombre del alumno: ", nombre_alumno)
print("Calificacion: ", calificacion)
print("Materia: ", materia)

print("Cadena original: ", cadena_original)
print("Cadena volteada: ", cadena_volteada)