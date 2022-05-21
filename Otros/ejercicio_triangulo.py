n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):  #j empezará en el rango de i,despues le restará 2 y terminará en la posicion 0 que es 1
        print(j, end=" ")
    print("")