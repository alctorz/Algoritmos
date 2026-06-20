"""
4- Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
   sus nombres y puntajes promedio obtenidos (de 1 a 10).
   Cargar sus datos en vectores paralelos, mostrar docente con calificación más
   alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
   calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
   desaprobaron (tomando como base que se aprueba con una nota mayor o
   igual a 6)
"""

docentes = []
puntajes = []

for x in range(6):
    nombre = input("Ingrese el nombre del docente: ")
    puntaje = int(input("Ingrese el puntaje promedio del docente (de 1 a 10): "))
    docentes.append(nombre)
    puntajes.append(puntaje)

maxima = max(puntajes)
minima = min(puntajes)

for x in range(6):
    if puntajes[x] == maxima:
        print(f"El docente con la calificación más alta es: {docentes[x]} con un puntaje de {puntajes[x]}")
    if puntajes[x] == minima:
        print(f"El docente con la calificación más baja es: {docentes[x]} con un puntaje de {puntajes[x]}")

print("Lista ordenada de mayor a menor según las calificaciones:")

for x in range(6):
    for z in range(x + 1, 6):
        if puntajes[x] < puntajes[z]:
            aux = puntajes[x]
            puntajes[x] = puntajes[z]
            puntajes[z] = aux
            aux = docentes[x]
            docentes[x] = docentes[z]
            docentes[z] = aux

for a in range(6):
    print(f"{docentes[a]}: {puntajes[a]}")

aprobados = 0
desaprobados = 0

for x in range(6):
    if puntajes[x] >= 6:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1

print(f"Cantidad de docentes que aprobaron: {aprobados}")
print(f"Cantidad de docentes que desaprobaron: {desaprobados}")