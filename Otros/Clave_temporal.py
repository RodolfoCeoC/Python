import os
from datetime import datetime

datos_contra = []
bienvenida = """La contraseña es: 

El nombre de tu animal favorito(al revés)
+ Las iniciales de tu nombre junto con los apellidos
+ La hora actual en horario de verano(Solo hora y minutos en formato de 24 horas.Ejemplo: 14:30).
"""

fecha = datetime.now()
hora = fecha.hour + 1
minutos = fecha.minute

animal_fav = input("Cual es tu animal favorito?: ")
animal_fav_invert = animal_fav[::-1]
nombre = input("Ingresa tu nombre: ")
dividir_nombre = nombre.split(" ")

if len(dividir_nombre) == 1:
    datos_contra.append(dividir_nombre[0][0])

elif len(dividir_nombre) >=2:
    for i in dividir_nombre:
        for j in i[0]:
            datos_contra.append(j)

datos_contra_string = "".join(datos_contra)

clave_temporal = f'{animal_fav_invert}{datos_contra_string}{hora}:{minutos}'

print()
print(bienvenida)

while True:
    
    contra = input("Ingresa la contraseña\n>>")

    if contra == clave_temporal:
        os.startfile('C:\\Users\\screa\\Escritorio\\mensaje.txt') #Ruta con un archivo txt(puede reemplazarse por otra ruta o por otro archivo)
        break
    
    else:
        print("No digas mamadas mary jane")