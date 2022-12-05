import keyboard
import time

segundos = int(input("Ingrese la cantidad de segundos que desee bloquear el teclado: "))

for i in range(150):
    keyboard.block_key(i)
    
time.sleep(segundos)