dict = {}

while True:
    pregunta = input("¿Quieres ingresar algun elementro al diccionario?: ")
    if pregunta == "si":
        elemento = input("Ingresa un elemento al diccionario: ")
        dato = input("Ingrese el valor del elemento: ")
        dict[elemento] = dato
        print(dict)
    elif pregunta == "no":
        print("Dentro del diccionario hay " + str(len(dict)),"elementos","y son " + str(dict))
        break