traductor = {}
continuar = True

while continuar:
    word = input("Ingrese una palabra en ingles y su significado en español(separadas por dos puntos): ")
    continuar = input("Desea agregar otra palabra?: ") == 'si'
    word_1 = word.split(':')
    traductor[word_1[0]] = word_1[1]

palabra = input("Ingrese la palabra en ingles que desea traducir: ")
for i in palabra.split():
    if i in traductor:
        print(traductor[i].capitalize(), end=" ")
    else:
        print("La palabra no esta disponible en el diccionario")



