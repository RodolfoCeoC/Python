
def factorial():
    numero = int(input("Ingresa un numero: "))
    temp = 1                 #Creamos una variable temporal que empezara desde el 1
    for i in range(numero):  #Usamos un for en donde la variable i va a iterar los numeros segun el rango establecido
        temp *= i+1          #La variable temporal va iniciar desde el 1 multiplicando todos los números hasta el rango de i
        result = "El factorial de: {} es: {}".format(numero, temp) #Usamos un format para almacenar el número ingresado y el factorial de ese número
    return result

print(factorial())