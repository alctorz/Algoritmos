"""
4- Crear dos listas paralelas. En la primera ingresar los nombres de empleados y
   en la segunda los sueldos de cada empleado.
   Ingresar por teclado cuando inicia el programa la cantidad de empleados de la
   empresa.
   Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el
   sueldo como su nombre)
"""

empleados = []
sueldos = []

emp = int(input("Ingrese la cantidad de empleados: "))

for x in range(emp):
  nom = input("Ingrese el nombre del empleado: ")
  empleados.append(nom)
  sueldo = int(input("Ingrese el sueldo del empleado: "))
  sueldos.append(sueldo)

for x in range(len(empleados) - 1, -1, -1):
  if sueldos[x] > 10000:
    empleados.pop(x)
    sueldos.pop(x)

print("Empleados con sueldo menor o igual a 10000:")
for x in range(len(empleados)):
  print(empleados[x], "-", sueldos[x])