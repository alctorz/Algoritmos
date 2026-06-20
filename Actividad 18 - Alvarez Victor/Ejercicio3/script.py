"""
3- Confeccionar una función que calcule la superficie de un rectángulo y la
   retorne, la función recibe como parámetros los valores de dos de sus lados:
   def retornar_superficie(lado1,lado2):
   En el bloque principal del programa cargar los lados de dos rectángulos y
   luego mostrar cuál de los dos tiene una superficie mayor.
"""

def retornar_superficie(lado1, lado2):
   return lado1*lado2

def valores():
   lado1 = int(input("Ingrese el primer lado del rectángulo: "))
   lado2 = int(input("Ingrese el segundo lado del rectángulo: "))
   return retornar_superficie(lado1, lado2)

superficie1 = valores()
superficie2 = valores()

if superficie1>superficie2:
   print("El primer rectángulo tiene una superficie mayor.")
elif superficie2>superficie1:
   print("El segundo rectángulo tiene una superficie mayor.")
else:
   print("Los dos rectángulos tienen la misma superficie.")