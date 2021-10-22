codigo=["A0-01","A0-02","A0-03","A0-04","A0-05"]
producto=["Shampoo","Cepillo","Colinos","Jabon","Enjuague bocal"]
precio=[20,7,13,12,16]
ingreso=[]
cantidad=[]
subtotal = 0

print('-' * 60)
print('-' * 15 + 'BIENVENIDOS A ESTA APLICACION' + '-' * 16)
print('-' * 60)
nombre=input("Ingrese nombre del cliente: ")
respuesta = 'si'
while respuesta == 'si':
    print('-' * 5 + 'Lista de productos' + '-' * 37)
    for i in range(len(producto)):
        print("{:<15} {:<15} {:<115}".format(codigo[i], producto[i], precio[i]))
    print('-' * 60)
    prod = input('Ingrese producto: ')
    can = int(input('Ingrese la cantidad: '))
    for item in codigo:
        if item == prod:
            ingreso.append(prod)
            cantidad.append(can)
            mensaje='Producto agregado'
            break
        else:
            mensaje='Codigo de producto incorrecto'
            respuesta='si'
    respuesta = input('Desea continuar (si/no): ')
    if respuesta=='no':
        break

for j in range(len(ingreso)):
    indice = codigo.index(ingreso[j])
    multi = precio[indice] * cantidad[j]
    subtotal = subtotal + multi

igv = round(subtotal * 0.18,2)
total = subtotal - igv

print('-' * 60)
print('-' * 27 + 'BOLETA' + '-' * 27)
print('-' * 60)
print(f'{nombre} su boleta es:')
print(f'Subtotal: {subtotal}')
print(f'IGV: {igv}')
print(f'Total: {total}')
print('-' * 60)

#trabajoterminado

