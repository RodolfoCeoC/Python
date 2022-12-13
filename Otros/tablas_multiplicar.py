
INICIO = 1
FIN = 10

numero = int(input("Que tabla de multiplicar buscas? : "))

for i in range(INICIO, FIN + 1):
    print(str(numero) + " X " + str(i) + " = " + str(numero * i))