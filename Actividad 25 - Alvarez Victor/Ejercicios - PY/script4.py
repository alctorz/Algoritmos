"""
4-  Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
    hardware.
    - Crear una lista donde cada elemento sea una tupla de tres elementos que
      represente: (nombre_articulo, precio, stock).
    Desarrollar las siguientes funciones:
    1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
       armar las tuplas correspondientes.
    2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
       artículos desempaquetando la tupla de manera directa en el bucle for.
    3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
       (sumando el resultado de precio * stock de cada uno de los componentes).
    4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
       sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
"""

def cargar():
  lista = []
  for x in range(5):
    nombre_articulo = (input(f"Ingrese el nombre del artículo {x+1}: "))
    precio = int(input(f"Ingrese el precio del artículo {x+1}: "))
    stock = int(input(f"Ingrese el stock del artículo {x+1}: "))
    lista.append((nombre_articulo, precio, stock))
  return lista

def imprimir_listado(lista):
   print("Listado de artículos:")
   for nombre_articulo, precio, stock in lista:
      print(f"Nombre: {nombre_articulo}, Precio: {precio}, Stock: {stock}")

def valor_inventario(lista):
   total = 0
   for nombre_articulo, precio, stock in lista:
      total += precio * stock
   print(f"Valor total del inventario: {total}")

def alerta_reposicion(lista):
   print("Artículos con stock menor o igual a 10 unidades:")
   for nombre_articulo, precio, stock in lista:
      if stock <= 10:
         print(f"Nombre: {nombre_articulo}, Stock: {stock}")

lista = cargar()
imprimir_listado(lista)
valor_inventario(lista)
alerta_reposicion(lista)