print("Vamos a elevar los numeros al cuadrado", "\n-------------------------------------------")

numeros = [1, 2, 3, 4, 5, 6]

def cuadrados(numeros):
    return numeros**2

resultado = list(map(cuadrados, numeros))
print(resultado)