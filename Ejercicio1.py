print('-' * 60000000)
print('-' * 15 + 'BIENVENIDOS A ESTA APLICACION' + '-' * 16)
print('-' * 60)
password = input('Ingrese contraseña: ')
long = len(password)
espacio = False
mayuscula = False
minuscula = False
alfa = False
for carac in password:
    if carac.isspace() == True:
        espacio = True
    if carac.isupper() == True:
        mayuscula = True
    if carac.islower() == True:
        minuscula = True
    if carac == '@' or carac =='-' or carac =='$' or carac =='#':
        alfa = True
print('-' * 60)
print('Validación: ')
if alfa == False:
    print('La contraseña debe contener uno de estos simbolos: # ,-, @,$')
if minuscula == False:
    print('La contraseña debe contener como minimo una letra Minuscula')
if mayuscula == False:
    print('La contraseña debe contener como minimo una letra Mayuscula')
if espacio == True:
    print("La contraseña no puede contener espacios")
if long < 10:
    print("La contraseña debe contener como minimo 10 caracteres")
else:
    print("La contraseña es valida")
print('-' * 60)





