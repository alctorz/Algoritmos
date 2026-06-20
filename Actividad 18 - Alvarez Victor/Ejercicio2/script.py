"""
2- Confeccionar una función que reciba tres enteros y los muestre ordenados
   de menor a mayor. En otra función solicitar la carga de 3 enteros por
   teclado y proceder a llamar a la primer función definida.
"""

def ordenar(v1, v2, v3):
   if v1<v2 and v1<v3:
      print(v1)
      if v2<v3:
         print(v2)
         print(v3)
      else:
         print(v3)
         print(v2)
   elif v2<v1 and v2<v3:
      print(v2)
      if v1<v3:
         print(v1)
         print(v3)
      else:
         print(v3)
         print(v1)
   elif v3<v1 and v3<v2:
      print(v3)
      if v1<v2:
         print(v1)
         print(v2)
      else:
         print(v2)
         print(v1)

def valores():
   valor1 = int(input("Ingrese el primer valor: "))
   valor2 = int(input("Ingrese el segundo valor: "))
   valor3 = int(input("Ingrese el tercer valor: "))
   ordenar(valor1, valor2, valor3)

valores()