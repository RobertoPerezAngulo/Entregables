# Generaciones digitales
# Autor: Jose Roberto Perez Angulo
# Fecha: 05/07/2023
import datetime

edad= int(input('¿Cual es tu edad?:  '))

anio = int(datetime.datetime.now().year) - int(edad)


# Expresiones enidadas
if anio in range(1920,1940):
    print('Perteneces a la generacion "SILENT GENERATION"')
elif anio in range(1946,1964):
    print('Perteneces a la generacion "BABY BOOM"')
elif anio in range(1965,1979):
    print('Perteneces a la generacion "GENERACION X"')
elif anio in range(1980,2000):
    print('Perteneces a la generacion "MILLENNIALS"')
elif anio in range(2001,2010):
    print('Perteneces a la generacion "GENERACION Z"')
else:
    print('No se encontro tu generacion')