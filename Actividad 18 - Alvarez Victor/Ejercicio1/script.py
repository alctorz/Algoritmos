"""
1- Desarrollar un programa que solicite la carga de tres valores y muestre el
   menor. Desde el bloque principal del programa llamar 2 veces a dicha
   función (sin utilizar una estructura repetitiva)
"""

def menores(v1, v2, v3):
   if v1<v2 and v1<v3:
      print(v1)
   elif v2<v1 and v2<v3:
      print(v2)
   elif v3<v1 and v3<v2:
      print(v3)

def valores():
   valor1 = int(input("Ingrese el primer valor: "))
   valor2 = int(input("Ingrese el segundo valor: "))
   valor3 = int(input("Ingrese el tercer valor: "))
   menores(valor1, valor2, valor3)

valores()