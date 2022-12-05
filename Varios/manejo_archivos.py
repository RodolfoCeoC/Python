nombre = input("Ingresa el nombre que se almacenará\n>>")

file = open("nombres.txt","w")
file.write(nombre)
file.close()