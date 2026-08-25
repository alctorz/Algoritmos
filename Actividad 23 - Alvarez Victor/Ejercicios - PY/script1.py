"""
1-                          Sistema de Reserva de Butacas (Matrices 2D)
    Contexto: Un cine necesita un módulo automatizado para vender entradas. La sala se
              representa como una matriz (lista de listas) de N filas por M columnas, donde un 0
              representa un asiento libre y un 1 uno ocupado.
    Consigna: Escribir una función llamada reservar_consecutivos(sala, fila, cantidad) que reciba
              la matriz de la sala, el número de fila deseado y la cantidad de entradas que desea
              comprar el grupo de clientes.
    Requisitos:
        ● Debe buscar si existen suficientes asientos libres y contiguos (juntos) en esa
          misma fila.
        ● Si los encuentra, debe cambiar sus valores a 1 (ocupados) y retornar un mensaje
          confirmando la reserva con los números de columna asignados.
        ● Si no hay espacio consecutivo suficiente, debe indicar que no fue posible realizar la
          reserva sin modificar la sala.
          Ejemplo de Entrada:
          Sala de 3x5. En la fila 0, la columna 1 ya está ocupada: [ [0, 1, 0, 0, 0], ... ]
          Intentar reservar 3 asientos en la fila 0.
          Salida Esperada: Confirmación de reserva para las columnas 2, 3 y 4.
"""

def reservar_consecutivos(sala, fila, cantidad):
    for x in range(len(sala[fila]) - cantidad + 1):
        se_puede = True
        for z in range(cantidad):
            if sala[fila][x + z] == 1:
                se_puede = False

        if se_puede:
            columnas = []

            for z in range(cantidad):
                sala[fila][x + z] = 1
                columnas.append(x + z)

            return "Reserva realizada en las columnas " + str(columnas)

    return "No se pudo hacer la reserva."

sala = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

print("Sala antes:")
for fila in sala:
    print(fila)

print(reservar_consecutivos(sala, 0, 3))

print("Sala después:")
for fila in sala:
    print(fila)