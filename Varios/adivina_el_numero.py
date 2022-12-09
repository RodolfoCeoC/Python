#Juego de adivinar numeros

import random

init_num = 1   
max_num = 30

mensaje = f'Adivina el numero que está entre el {init_num} y el {max_num}'
       
numero_aleatorio = random.randint(init_num, max_num)
print("\n" + mensaje + "\n")

while True:
    numero = int(input("Ingresa un numero: "))
    if numero == numero_aleatorio:
        print("Felicidades, ganaste!")
        break
        
    elif numero < numero_aleatorio:
        print("Es mas!")
        
    elif numero > numero_aleatorio:
        print("Es menos!")