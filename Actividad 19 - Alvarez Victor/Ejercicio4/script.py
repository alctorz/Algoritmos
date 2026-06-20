"""
4- Elaborar una función que muestre la tabla de multiplicar del valor que le
   enviemos como parámetro. Definir un segundo parámetro llamado termino
   que por defecto almacene el valor 10. Se deben mostrar tantos términos de
   la tabla de multiplicar como lo indica el segundo parámetro.
   Llamar a la función desde el bloque principal de nuestro programa con
   argumentos nombrados.
"""

def cargarValor():
   valor = int(input("Ingrese un valor a ser multiplicado: "))
   return valor


def tablaMultiplicar(num, valor = 10):
   aux = 1
   lista = []
   x = 1
   while x <= valor:
      valorLista = num * aux
      lista.append(valorLista)
      aux = aux + 1
      x = x + 1
   return lista

numero=cargarValor()
print(f"Tabla de Multiplicar de {numero}")
print("*********************************")
print(tablaMultiplicar(numero))