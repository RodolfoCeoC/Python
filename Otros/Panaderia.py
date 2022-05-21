barras_pan = 3.49
pan_con_descuento = barras_pan * 0.6
descuento = barras_pan - pan_con_descuento
venta = int(input("Ingrese el total de barras de pan: "))
operacion = pan_con_descuento * venta
print("El precio normal de una barra de pan es de 3.49 euros")
print("Usted compró " + str(venta) + " barras de pan")
print("El precio total normal seria de: " + str((barras_pan * venta).__round__(2)) + " euros" +
      " pero su descuento es del 60%: " + str((descuento * venta).__round__(2)) + " euros")
print("Asi que por el dia de hoy su pago total es de: " + str(operacion.__round__(2)) + " euros")
print("Ay que nervios ya estoy practicando.jpg")