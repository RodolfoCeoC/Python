moneda = {'Dolar':'$', 'Yen':'y'}
pregunta = input("Escriba alguna moneda para devolver su simbolo: ")

if pregunta == 'dolar':
    print(moneda['Dolar'])
elif pregunta == 'yen':
    print(moneda['Yen'])
else:
    print("Esa modena no existe en el diccionario")

moneda = {'Dolar':'$', 'Yen':'y'}
pregunta = input("Ingrese un simbolo: ")

print(moneda.get(pregunta.title()))