print("¡Bienvenidos a su pizzeria favorita!", "\n----------------------------------------------------")
pizza = input("¿Quieres una pizza vegerariana? Responde 'si' o 'no': ")
vegetarianas = ["Pimiento", "Tofu"]
No_vegetarianas = ["Peperoni", "Jamón", "Salmón"]
ingredientes_base = "Tomate, Mozarella "

if pizza == 'si':
    print("Los ingredientes vegetarianos son: " + str(vegetarianas))
    ingrediente = input("Elige un ingrediente: ")
    if ingrediente == "pimiento":
        print("Los ingredientes son: " + ingredientes_base + "y " + vegetarianas[0])
    elif ingrediente == "tofu":
        print("Los ingredientes son: " + ingredientes_base + "y " + vegetarianas[1])
    else:
        print("Esa opcion no existe")

if pizza == 'no':
    print("Los ingredientes normales son:" + str(No_vegetarianas))
    ingredientes_normales = input("Elige un ingrediente: ")
    if ingredientes_normales == "peperoni":
        print("Los ingredientes de su pizza son: " + ingredientes_base + "y " + No_vegetarianas[0])
    elif ingredientes_normales == 'jamon':
        print("Los ingredientes de su pizza son " + ingredientes_base + "y " + No_vegetarianas[1])
    elif ingredientes_normales == 'salmon':
        print("Los ingredientes de su pizza son: " + ingredientes_base + "y " + No_vegetarianas[2])
    else:
        print("Elige una opcion correcta")