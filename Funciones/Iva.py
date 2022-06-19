
def porcentaje_iva():
    cantidad = float(input("Ingrese una cantidad: "))
    iva = float(input("Ingrese el iva: "))
    operacion = ((iva / 100) * cantidad) + cantidad
    return operacion

print(porcentaje_iva())
