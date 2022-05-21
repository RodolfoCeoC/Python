punto_1 = [1, 2, 3]
punto_2 = [-1, 0, 2]
producto_punto = []
contador = 0
for i, j in zip(punto_1, punto_2):
    operacion = i * j
    producto_punto.append(operacion)
# print(sum(producto_punto)) Funcion automatica para sumar los elementos de una lista

for suma in producto_punto:
    contador += suma
print("El producto punto de " + str(punto_1), " y " + str(punto_2), "es " + str(contador))