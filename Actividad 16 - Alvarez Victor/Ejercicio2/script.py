"""
2- Una empresa registra los nombres de sus 5 vendedores y el total de ventas
   realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
   vectores paralelos, ordenar los datos de mayor a menor según las ventas,
   imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
   el que menos vendió de los 5 empleados. 
"""

vendedores = []
ventas = []

for x in range(5):
    nombre = input("Ingrese el nombre del vendedor: ")
    venta = float(input("Ingrese el total de ventas del vendedor: "))
    vendedores.append(nombre)
    ventas.append(venta)

for x in range(5):
    for z in range(x + 1, 5):
        if ventas[x] < ventas[z]:
            aux = ventas[x]
            ventas[x] = ventas[z]
            ventas[z] = aux
            aux = vendedores[x]
            vendedores[x] = vendedores[z]
            vendedores[z] = aux

print("Lista ordenada de mayor a menor según las ventas:")
for a in range(5):
    print(f"{vendedores[a]}: {ventas[a]}")

print(f"El vendedor que menos vendió fue: {vendedores}")