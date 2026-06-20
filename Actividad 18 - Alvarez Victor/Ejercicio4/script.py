"""
4- Plantear una función que reciba un string en mayúsculas o minúsculas y
   retorne la cantidad de letras "a" o "A".
"""

def contar_a(cadena):
   contador = 0
   for letra in cadena:
      if letra == "a" or letra == "A":
         contador = contador + 1
   return contador

cadena = input("Ingrese una cadena de texto: ")
cantidad_a = contar_a(cadena)
print(f"La cantidad de letras 'a' o 'A' en la cadena es: {cantidad_a}")