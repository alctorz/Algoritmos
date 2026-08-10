"""
5-                          Gestión de Triaje en Guardia Médica (Prioridad)
    Contexto: Un hospital atiende pacientes según la gravedad de su condición (Triaje), no
    únicamente por orden de llegada. Los niveles de urgencia son: 1 (Normal), 2 (Moderado) y 3
    (Crítico).
    Consigna: La sala de espera se representa como una lista de registros sin diccionarios:
              [["Paciente", Prioridad], ...]. Crear la función atender_siguiente(cola_espera)
              que seleccione al próximo paciente en ser atendido.
    Requisitos:
        ● Buscar al paciente que posea la prioridad más alta (mayor número).
        ● En caso de empate en la prioridad, se debe atender al primero que haya llegado a
          la guardia (criterio FIFO).
        ● Eliminar al paciente seleccionado de la lista de espera y devolver un mensaje
          indicando su nombre y nivel de urgencia.
          Ejemplo de Entrada: [["Carlos", 1], ["Ana", 3], ["Roberto", 2], ["Lucía", 3]] Salida
                              Esperada: Atiende primero a Ana (Nivel 3). Si se vuelve a llamar a la función,
                              la siguiente será Lucía (Nivel 3).
"""

def atender_siguiente(cola_espera):
    if len(cola_espera) == 0:
        return "No hay pacientes en espera."

    mayor = 0

    for x in range(len(cola_espera)):
        if cola_espera[x][1] > cola_espera[mayor][1]:
            mayor = x

    paciente = cola_espera.pop(mayor)

    return "Atiende primero a " + paciente[0] + " (Nivel " + str(paciente[1]) + ")"

cola = [
    ["Carlos", 1],
    ["Ana", 3],
    ["Roberto", 2],
    ["Lucía", 3]
]

print(atender_siguiente(cola))
print(atender_siguiente(cola))

print("Pacientes restantes:")
print(cola)