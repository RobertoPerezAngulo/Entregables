#Autor : Jose Roberto Perez Angulo
#Fecha : 18/09/2021

#Realizar una funcion llamada año_bisiesto
# Recibira un año por parametro
# Imprimira el año bisiesto
# El anio no es bisiesto
# Si se ingresa algo que no sea numero, sera ingrese un numero

def año_besiesto():
    anio = input('Ingresa un número: ')
    if(anio.isnumeric() == False):
        print('Ingresa un número no una letra')
    elif(int(anio) % 4 == 0):
        print('El año es bisiesto')
    else:
        print('El año no es bisiesto')
    
    repeat = input('Desea repetir la funcion S/N:')
    año_besiesto() if repeat.upper().__eq__('s'.upper())  else exit() 


año_besiesto()