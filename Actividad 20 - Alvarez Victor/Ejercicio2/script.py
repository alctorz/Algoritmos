"""
2- Desarrollar una aplicación que permita ingresar por teclado los nombres de
   5 artículos y sus precios.
   Definir las siguientes funciones:
    1) Cargar los nombres de artículos y sus precios.
    2) Imprimir los nombres y precios.
    3) Imprimir el nombre de artículo con un precio mayor
    4) Ingresar por teclado un importe y luego mostrar todos los artículos con
       un precio menor igual al valor ingresado.
"""

def articulosPrecios(nom, precio):
   for x in range(5):
      valor1 = input(f"Ingrese el nombre del articulo n{x}: ")
      nom.append(valor1)
      valor2 = int(input(f"Ingrese el precio de {nom[x]}: "))
      precio.append(valor2)
   return nom, precio


def precioMayor(li):
   mayor = 0
   for x in range(5):
      if li[x] > mayor:
         mayor = li[x]
         nomMay = nombres[x]
   return nomMay

def importe(lu):    
   nomm = []
   imprt = int(input("Ingrese un importe: "))
   for x in range(5):        
      if lu[x] < imprt:
         imprt = lu[x]
         nomm.append(nombres[x])
   return nomm

nombres = []
precios = []

lista = articulosPrecios(nombres, precios)
print(lista)

alto = precioMayor(precios)
print(f"El precio mayor es: {alto}")

bajo = importe(precios)
print(f"Los precios menores son: {bajo}")