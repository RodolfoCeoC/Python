materias = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}
cred = []

for i in materias:
    creditos = materias.get(i)
    cred.append(creditos)
    print(i,"tiene: " + str(creditos),"creditos")

contador = 0

for j in cred:
    contador += j

print("Los creditos totales son: " + str(contador))
