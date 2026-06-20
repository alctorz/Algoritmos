"""
2- En una empresa se almacenaron los sueldos de 10 personas.
   Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
   1) Carga de los sueldos en una lista.
   2) Impresión de todos los sueldos.
   3) Cuántos tienen un sueldo superior a $4000.
   4) Retornar el promedio de los sueldos.
   5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargarSueldos():
   lista = []
   for x in range(10):
      sueldo = int(input(f"Ingrese el sueldo del empleado n°{x}: "))
      lista.append(sueldo)
   return lista

def superior(li):
   contador = 0
   for x in range(len(li)):
      if li[x] > 4000:
         contador = contador + 1
   return contador

def promedio(li):
   promedio = 0
   for x in range(len(li)):
      promedio = promedio + li[x]
   promedio = promedio / 10
   return promedio

def sueldosBajos(li):
   prom = promedio(lista)
   listaPromedios = []
   for x in range(len(li)):
      if li[x] < prom:
         valor = li[x]
         listaPromedios.append(valor)
   return listaPromedios

lista = cargarSueldos()
print(lista)
print(f"La cantidad de empleados con un sueldo mayor a $4000 es: {superior(lista)}")
print(f"El promedio de los sueldos de los empleados es: {promedio(lista)}")
print(f"Los sueldos que están por debajo del promedio son: {sueldosBajos(lista)}")