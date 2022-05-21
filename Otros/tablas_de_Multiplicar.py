# tablas de multiplicar del 1 a 10
# Creamos un for con los numeros principales que son del 1 al 10
# Luego creamos otro for dentro del for en donde los numeros seran por los que se van a multiplicar

for i in range(1, 11):
    for j in range(1, 11):
        print(str(j) + " X " + str(i) + " = " + str(i*j), end="\t")
    print("")