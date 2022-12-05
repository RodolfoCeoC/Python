#Numeros pseudoaleatorios del 0 al 9
from datetime import datetime

def aleatorio():
    fecha = datetime.now()
    microsegundos = fecha.microsecond
    lista_microsec = [int(i) for i in str(microsegundos)]
    posicion = lista_microsec[0]
    return posicion
print(aleatorio())
