print("Nivel " "Puntuacion ","\n______________________", "\nInaceptable ", " 0.0",
      "\nAceptable ", " 0.4", "\nMeteorito ", "0.6 o mas")
print("_______________________")

puntuacion = float(input("Ingrese su puntuacion: "))
dinero = 2400
if puntuacion == 0.0:
    print("Tu rendimiento es una blasfemima para la empresa, tu dinero obtenido es de: " + str(dinero*puntuacion))
elif puntuacion == 0.4:
    print("Tu rendimiento podria mejorar, tu dinero obtenido es de: " + str(dinero*puntuacion))
elif puntuacion == 0.6:
    print("Eres un alfa, tu dinero obtenido es de: " + str(dinero*puntuacion))
else:
    print("Favor de ingresar datos correctos")