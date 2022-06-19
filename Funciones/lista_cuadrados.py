
numeros = [1, 2, 3, 4, 5]

def cuadrado(elevar):
    return elevar ** 2

numeros_cuadrado = map(cuadrado, numeros)
print(list(numeros_cuadrado))
