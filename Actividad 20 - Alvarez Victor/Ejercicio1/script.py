"""
1- Desarrollar una función que reciba una lista de string y nos retorne el que
   tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
   debe retornar el que tiene un valor de componente más baja.
   En el bloque principal iniciamos por asignación la lista de string:
   palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
   print("Palabra con más caracteres:",mascaracteres(palabras))
   (La lista debe tener la misma cantidad de elementos, pero los textos los
   eligen ustedes)
"""

def masCaracteres(palabra):
   mayor = palabra[0]
   for x in range(1, 5):        
      if len(mayor) < len(palabra[x]):
         mayor = palabra[x]
   return mayor

lista=["enero", "febrero", "marzo", "abril", "mayo", "junio"]

print(f"Palabra con más caracteres: {masCaracteres(lista)}")