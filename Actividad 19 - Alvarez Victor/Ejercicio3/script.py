"""
3- Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
   debe retornar la suma de dichos valores. Debe tener tres parámetros por
   defecto.
"""

def suma(li = [9, 7, 2, 23], suma = 0, x = 0):
    while x < 4:
        suma = suma + li[x]
        x = x + 1
    return suma

print(f"La suma de los valores es: {suma()}")