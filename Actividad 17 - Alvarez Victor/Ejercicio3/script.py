"""
3- Definir una lista y almacenar los nombres de 3 empleados.
   Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
   números de días del mes que el empleado faltó.
   Imprimir los nombres de empleados y los días que faltó.
   Mostrar los empleados con la cantidad de inasistencias.
   Finalmente mostrar el nombre o los nombres de empleados que faltan menos
   días.
"""

empleados = []
faltas = []

for x in range(3):
  nom = input("Ingrese el nombre del empleado: ")
  empleados.append(nom)
  faltas_empleado = []
  for x in range(30):
    falta = int(input("Ingrese el número del día que el empleado faltó (0 para terminar): "))
    if falta == 0:
      break
    faltas_empleado.append(falta)
  faltas.append(faltas_empleado)

print("Empleados y días que faltaron:")

for x in range(3):
  print(empleados[x], "faltó los días:", faltas[x])

print("Empleados con la cantidad de inasistencias:")

for x in range(3):
  print(empleados[x], "faltó", len(faltas[x]), "días")

minimo = min(len(faltas[x]) for x in range(3))

print("Empleados que faltaron menos días:")

for x in range(3):
  if len(faltas[x]) == minimo:
    print(empleados[x])