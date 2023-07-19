# Aprobacion de credito bancario
# Autor: Jose Roberto Perez Angulo
# Fecha: 05/07/2023

#Recursos del sistema
socios = [
    {
        'nombre': 'Juan',
        'edad': 27,
        'ingreso': 10000,
        'antiguedad' : 10
    },
    {
        'nombre': 'Pedro',
        'edad': 35,
        'ingreso': 65000,
        'antiguedad' : 3
    }
]



# Variables
nombre = input('¿Cual es tu nombre?:  ')
edad = int(input('¿Cual es tu edad?:  '))
ingreso = float(input('¿Cual es tu ingreso mensual?:  '))


#Funciones de validacion
def valida_persona():
    if nombre.__eq__(''):
        print('El nombre no puede estar vacio')
        exit();
    elif edad < 18:
        print('No puedes solicitar un credito porque eres menor de edad')
        exit();
    elif ingreso <= 10000:
        print('No puedes solicitar un credito debido a que tu ingreso es menor a 10000')
        exit();
    else:
        print('Felicidades, tu credito ha sido aprobado')


# Proximas validaciones
for socio in socios:
    if nombre in socio['nombre'] :
        print('Ya eres socio')
        valida_persona()
        exit();
else:
    print('No eres socio registrado en la base de datos');

def ingresaComprador():
    socios.append({
        'nombre': nombre,
        'edad': edad,
        'ingreso': ingreso
    })
    print('Bienvenido nuevo socio')


def eliminaComprador():
    socios.remove({
        'nombre': nombre,
        'edad': edad,
        'ingreso': ingreso
    })
    print('Socio eliminado')


def actualizaComprador():
    socios.update({
        'nombre': nombre,
        'edad': edad,
        'ingreso': ingreso
    })
    print('Socio actualizado')

def actualizaNombre():
    socios.update({
        'nombre': nombre
    })
    print('Nombre actualizado')


def consultaComprador():
    print(socios)