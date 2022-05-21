asignaturas = ['Español', 'Matematicas', 'Historia', 'Geografia']
calif = []
for i in asignaturas:
    calificacion = input("¿Cuanto sacaste en " + i + "? :")
    calif.append(calificacion)

for j in range(len(asignaturas)):
    print("La calificacion obtenida en " + asignaturas[j] + " es: " + calif[j])