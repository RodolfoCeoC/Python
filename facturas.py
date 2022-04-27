# dict = {'Nombre': 'Rodolfo', 'Apellidos': 'Ceo Cortés'}
# dict.pop('Nombre') #pop permite borrar algun elemento del diccionario, para ellos colocamos dentro del parentesis la clave de referencia,
# print(di
dic_facturas = {}
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
        factura = input("Ingrese un numero de factura: ")
        cantidad = float(input("Ingrese una cantidad de pesos Mexicanos a su factura: "))
        dic_facturas[factura] = cantidad
        print("La factura numero " + factura,"con la cantidad de " + str(cantidad),"pesos se guardó con éxito")
        seguir = input("¿Deseas continuar?: ") == "si"

    elif selec == "2":
        if len(dic_facturas) == 0:
            print("No hay facturas disponibles, ingrese una nueva")
            seguir = input("¿Desea regresar al menú principal?: ") == "si"
        elif len(dic_facturas) != 0:
            print(dic_facturas)
            pagar = input("Escribe el número de la factura que deseas pagar: ")
            if pagar not in dic_facturas.keys():
                print("No se encuentra el elemento")
            else:
                print("Seguro quiere pagar la factura " + pagar)
                eliminar = dic_facturas.pop(pagar)
                print("¡La factura se pagó con exito!")
                seguir = input("¿Desea continuar?: ") == "si"

    else:
        print("_______________________________","\n¡La opción ingresada no existe!")
        seguir = input("¿Quieres volver a intentarlo?: ") == "si"
