nombres = set()
while nombres.__contains__('fin') == False:
    nombre = input('Ingrese un nombre: ')
    if nombre.__eq__('fin'):
        break 
    nombres.add(nombre)

print(nombres)


 



