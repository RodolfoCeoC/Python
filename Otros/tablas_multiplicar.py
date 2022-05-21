print("¡Volvamos a la primaria!" + "\n----------------------")
numero = int(input("¿Que tabla de multiplicar buscas? : "))
for i in range(1, 11):
    print(str(numero) + " X " + str(i) + " = " + str(numero*i))