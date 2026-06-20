"""
3- Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
   con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
   una tupla)
   El programa debe tener las siguientes funciones:
   1)Carga de los nombres de empleados y sus últimos tres sueldos.
   2)Imprimir el monto total cobrado por cada empleado.
   3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
     10000 en los últimos tres meses.
   Tener en cuenta que la estructura de datos si se carga por asignación debería ser
   similar a:
   empleados = [["juan",(2000,3000,4233)], ["ana",(3444,1000,5333)], etc ]
"""

def imprimir(Empleados):
    for x in range (len(Empleados)):
        print(f"Empleado: {Empleados[x][0]}")
        print("Últimos 3 sueldos:")
        for z in range(3):
            print(Empleados[x][1][z])
        print("----------------------------")

def monto_total(Empleados):
    suma = 0
    nombres = []
    for x in range (len(Empleados)):
        for z in range (3):
            suma = suma + Empleados[x][1][z]
        print(f"La suma total del empleado {x} es: {suma}")
        if suma > 10000:
            nombres.append(Empleados[x][0])
        suma = 0
    print(f"El/Los empleado/s con un ingreso trimestral mayor a 10000 es/son: {nombres}")

empleados = [["Juan",(2000, 3000, 4233)], ["Ana",(3444, 1000, 5333)], ["Cristian",(2999, 4100, 6700)], ["Bruno",(2100, 3010, 4321)], ["Luciano",(1234, 2345, 3456)]]

imprimir(empleados)
monto_total(empleados)