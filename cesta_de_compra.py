cesta = {}

seguir = True
while seguir:
    articulo = input("Ingrese un articulo a la cesta: ")
    precio = float(input("Ingrese su precio: "))
    cesta[articulo] = precio
    seguir = input("Desesa ingresar un articulo?: ") == "si"

contador = 0
print("Usted compró", "\n----------------------------------")
for i, j in cesta.items(): #permite dividir los elementos de una libreria, donde el primero es la clave y el segundo su valor.
    contador += j
    print(i.capitalize(),"\t", j, "\n----------------------------------")
print("El total a pagar es de " + str(contador),"pesos")
