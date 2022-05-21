payaso = 112
munieca = 75

payasos_vend = int(input("Ingrese la cantidad de payasos: "))
munieca_vend = int(input("Ingrese la cantidad de muñecas: "))


peso_total = ("El numero total de productos a enviar es de: " + str(payasos_vend + munieca_vend) + " (" + str(payasos_vend) + " payasos" + " y " +
              str(munieca_vend) +  " muñecas" + ")" + "\nEl peso total de los " + str(payasos_vend) + " payasos es de: " + str(float(payaso * payasos_vend)) + " gramos" +
              "\nEl peso total de las " + str(munieca_vend) + " muñecas es de: " +str(float(munieca * munieca_vend)) + " gramos" + "\nEl pesos total de las " +
              str(payasos_vend+munieca_vend) + " piezas es de: " + (str(float(payaso * payasos_vend) + (munieca * munieca_vend))) + " gramos")

print(peso_total)