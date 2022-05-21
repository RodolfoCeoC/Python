menu_clientes = """
1. Añadir cliente
2. Eliminar cliente
3. Mostrar cliente
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
        nif = input("Agrega un NIF: ")
        name = input("Ingresa un nombre: ")
        address= input("Ingresa una direccion: ")
        phone_number = input("Ingresa un numero de telefono: ")
        email = input("Ingresa un email: ")
        preference = input("¿Es un cliente preferente?: ")
        dic_2 = {'Nombre':name,'Direccion':address,'Numero_de_telefono':phone_number,'Correo':email,'Preferente':preference=="si"}
        dic_1[nif] = dic_2
        continuar = input("Deseas continuar?: ") == "si"

    elif opcion == "2":
        trash = input("Ingresa el numero del NIF que deseas eliminar: ")
        if trash not in dic_1.keys():
            print("¡No hay ningun cliente registrado!")
        else:
            dic_1.pop(trash)
            print("¡Cliente eliminado!")

    elif opcion == "3":
        cliente = input("Ingrese el nip del cliente para mostrar sus datos: ")
        if cliente not in dic_1.keys():
            print("El número de factura no se encontró")
        else:
            print('NIF:', cliente)
            for clave, valor in dic_1[cliente].items():
                print(clave.title() + ':', valor)

    elif opcion == "4":
        if len(dic_1) == 0:
            print("No hay ningun dato existente!")
        else:
            for clave, valor in dic_1.items():
                print(clave + ".", valor['Nombre'],"\n----------------")

    elif opcion == "5":
        for clave, valor in dic_1.items():
            if valor['Preferente']:
                print(clave, valor['Nombre'])

    elif opcion == "6":
        print("Adios")
        break



