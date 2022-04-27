
frutas = {
    'Platanos': 1.35,
    'Manzanas': 0.80,
    'Peras': 0.85,
    'Naranjas': 0.70
}

while True:
    pregunta = input("Que fruta desea comprar?: ")
    if pregunta.title() in frutas:
        kilos = float(input("Ingrese la cantidad de kilos: "))
        precio = frutas.get(pregunta.title())
        print("Usted llevará " + str(kilos), "kilos", "de " + pregunta.capitalize(), "y pagará " + str((precio * kilos).__round__(2)),
              "dolares")
        break
    else:
        print("La fruta no está disponible")






