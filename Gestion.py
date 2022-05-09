menu_clientes = """
1. Añadir cliente
2. Eliminar cliente
3. Mostrat cliente
4. Listar todos los clientes
5. Listar clientes preferentes
6. Terminar
"""

dic_1 = {}
continuar = True

while continuar:
    print(menu_clientes)
    opcion = input("Ingresa una opcion: ")
    if opcion == "1":
        while continuar:
            nif = input("Agrega un NIF: ")
            name = input("Ingresa un nombre: ")
            address= input("Ingresa una direccion: ")
            phone_number = input("Ingresa un numero de telefono: ")
            email = input("Ingresa un email: ")
            preference = input("¿Es un cliente preferente?: ")
            dic_2 = {'Nombre':name,'Direccion':address,'Numero_de_telefono':phone_number,'Correo':email,'Preferente':preference=="si"}
            dic_1[nif] = dic_2
            continuar = input("Deseas agregar otro cliente?") == "si"

    # elif opcion == "2":
    #     trash = input("Ingresa el numero del NIF que deseas eliminar: ")
    #     if trash not in dic_1.keys():
    #         print("¡No hay ningun cliente registrado!")
    #         dic_1.pop(trash)


