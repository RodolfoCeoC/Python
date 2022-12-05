#Juego de adivinar numeros
#Los errores se visualizarán con la cara de mr increible

import random

mensaje = """ 
    Bievenidos al juego:
    La mecánica consiste en adivinar números.
    Si adivinas el número ganas ok? """
    
numero_aleatorio = random.randint(1, 30)

while True:
    numero = int(input("Ingresa un numero: "))
    if numero == numero_aleatorio:
        print("Felicidades, ganaste!")
        break
        
    elif numero < numero_aleatorio:
        print("Es mas!")
        
    elif numero > numero_aleatorio:
        print("Es menos!")