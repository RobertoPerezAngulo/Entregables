# Declaracion de variables
letra = input('Ingrese una letra: ')


# Imprimir resultado
paises = [{
    'nombre': 'Mexico'},
    {'nombre': 'Colombia'}, 
    {'nombre': 'Peru'},
    {'nombre': 'Chile'},
    {'nombre': 'Argentina'},
    {'nombre': 'Ecuador'},
    {'nombre': 'Venezuela'},
    {'nombre': 'Guatemala'},
    {'nombre': 'Cuba'}]

#Condicones
if letra.__len__() < 1 or letra.isnumeric():
    print('No se puede ingresar un valor vacio o numero')
    exit();
else:
    for pais in paises:
        if letra in pais.get('nombre'):
            print(pais.get('nombre'))
    else:
        print('No se encontro ningun pais con esa letra')
                    