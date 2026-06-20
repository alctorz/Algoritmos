"""
1- Se desea desarrollar un programa que permita registrar los nombres y las
   calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
   nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
   estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
   máxima o mínima.
"""

nombres = []
calificaciones = []

for x in range(5):
    nom = input("Ingrese el nombre del estudiante: ")
    calif = float(input("Ingrese la calificación del estudiante: "))
    nombres.append(nom)
    calificaciones.append(calif)

maxima = max(calificaciones)
minima = min(calificaciones)

for x in range(5):
   if calificaciones[x] == maxima:
        print(f"El estudiante con la nota más alta es: {nombres[x]} con una calificación de {calificaciones[x]}")
   if calificaciones[x] == minima:
        print(f"El estudiante con la nota más baja es: {nombres[x]} con una calificación de {calificaciones[x]}")

   if calificaciones.count(maxima) > 1:
    print("Hay estudiantes con la misma nota máxima.")

   if calificaciones.count(minima) > 1:
    print("Hay estudiantes con la misma nota mínima.")