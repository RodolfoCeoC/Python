
name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
addess = input("Ingresa tu direccion: ")
phone_number = int(input("Ingresa tu numero de telefono: "))

dict = {
       'Nombre': name,
       'Edad': age,
       'Direccion': addess,
       'Numero': phone_number
       }

print(dict['Nombre'], " tiene " + str(dict['Edad']), " años", ",", " su dirección es "
      + dict['Direccion'], " y su numero de telefono es " + str(dict['Numero']))

