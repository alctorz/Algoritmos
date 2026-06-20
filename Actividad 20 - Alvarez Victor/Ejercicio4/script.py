"""
4- Confeccionar una función que reciba una serie de edades y me retorne la
   cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
   a la función)
"""

def edades(ed):
   contE = 0
   for x in range(len(ed)):
      if ed[x] >= 18:
         contE = contE + 1
   return contE

edad = [20,15,17,19,18,20]

print(f"Hay {edades(edad)} que son mayores o iguales a 18 años.")