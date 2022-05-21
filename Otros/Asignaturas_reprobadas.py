asignaturas = ['Programación Orientada a Eventos', 'Fisica Nuclear', 'Astrobiologia', 'Filosofia de la Ciencia', 'Termodinamica']
reprobadas = []
califi = []
for i in asignaturas:
    calificacion = int(input("Cuanto sacaste en " + i + "?: "))
    if calificacion < 7:
        reprobadas.append(i)
        califi.append(calificacion)
print("Reprobaste: ")
for j in reprobadas:
    print(j)