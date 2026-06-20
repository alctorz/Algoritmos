"""
1- Crear una lista de enteros por asignación. Definir una función que reciba
   una lista de enteros y un segundo parámetro de tipo entero. Dentro de la
   función mostrar cada elemento de la lista multiplicado por el valor entero
   enviado.
   lista=[3, 7, 8, 10, 2]
   multiplicar(lista,3)
"""

def multiplicados(li, val):
   multis = []
   multi=0
   for x in range(len(li)):
      multi = li[x] * val
      multis.append(multi)
   return multis

lista=[9, 3, 7, 2, 23]
valor = 3
print("La lista multiplicada por el segundo parámetro es: ")
print(multiplicados(lista, valor))