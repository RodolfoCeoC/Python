dic_facturas = {}
pago_total = []
bienvenidos = """
-----------------------------------------
   Bienvenidos a la gestión de facturas   
-----------------------------------------
   Ingrese una opción para continuar:
   __________________________________
   
   1. Añadir una factura
   2. Imprimir y Pagar facturas almacenadas
   3. Terminar
    """

seguir = True

while seguir:
    print(bienvenidos)
    selec = input("Ingrese un numero: ")
    if selec == "1":
        while seguir:
            factura = input("Ingrese un numero de factura: ")
            if factura not in dic_facturas.keys():
                cantidad = float(input("Ingrese una cantidad de pesos Mexicanos a su factura: "))
                dic_facturas[factura] = cantidad
                print("La factura numero " + factura, "con la cantidad de " + str(cantidad),
                      "pesos se guardó con éxito")
                seguir = input("¿Deseas continuar?: ") == "si"
                break
            else:
                print("¡La factura ya existe!")

    elif selec == "2":
        if len(dic_facturas) == 0:
            print("No hay facturas disponibles, ingrese una nueva")
        elif len(dic_facturas) != 0:
            numeros = [str(j) for j in dic_facturas.keys()]            #Este método permite agregar un for dentro de un while para poder
            numero_2 = [str(k) for k in dic_facturas.values()]         #iterar todos los elementos del diccionario
            elementos = 0
            while elementos < len(dic_facturas):                       #para esto utilizamos un for y un while al mismo tiempo
                print("Factura",numeros[elementos],"\t", numero_2[elementos],"pesos","\n--------------------------")
                elementos += 1                                         #Aquí termina este método
            pagar = input("Escribe el número de la factura que deseas pagar: ")
            if pagar not in dic_facturas.keys():
                print("No se encuentra el elemento")
            else:
                check = input("Seguro quiere pagar la factura " + pagar +" :")
                if check == "si":
                    pago = dic_facturas.get(pagar)
                    pago_total.append(pago)
                    dic_facturas.pop(pagar)
                    print("¡La factura se pagó con exito!")
                    print("El total pagado hasta ahora es de $" + str(sum(pago_total)),"pesos M.N","y la cantidad restante es de $"
                          + str(sum(dic_facturas.values())),"pesos M.N")
                else:
                    seguir = input("¿Deseas regresar al menu principal?: ") == "si"

    elif selec == "3":
        print("¡Hasta pronto!")
        break

    else:
        print("_______________________________", "\n¡La opción ingresada no existe!")
