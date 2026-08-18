"""
3-  Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
    en cada habitación de la casa.
    - Crear un diccionario donde la Clave sea el nombre del ambiente (ej: &quot;Cocina&quot;,
      &quot;Dormitorio&quot;) y el Valor sea una lista de tuplas, donde cada tupla represente un
      dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
    Desarrollar las siguientes funciones:
    1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
       ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
       operador decida no cargar más para ese ambiente.
    2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
       en Watts acumulado en cada una de ellas.
    3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
       energía consume de toda la casa (el valor máximo individual dentro de todas las
       listas del diccionario), indicando en qué habitación se encuentra.
"""

def cargar():
    ambientes = {}
    for x in range(3):
        ambiente = input(f"Ingrese el nombre del ambiente {x + 1}: ")
        dispositivos = []
        while True:
            nombre_dispositivo = input(f"Ingrese el nombre del dispositivo activo en {ambiente} (o 'fin' para terminar): ")
            if nombre_dispositivo.lower() == 'fin':
                break
            consumo_watts = float(input(f"Ingrese el consumo en Watts de {nombre_dispositivo}: "))
            dispositivos.append((nombre_dispositivo, consumo_watts))
        ambientes[ambiente] = dispositivos
    return ambientes

def consumo_por_habitacion(ambientes):
    for ambiente in ambientes:
        dispositivos = ambientes[ambiente]
        consumo_total = sum(consumo for _, consumo in dispositivos)
        print(f"El consumo total en {ambiente} es: {consumo_total} Watts")

def dispositivo_critico(ambientes):
    max_consumo = 0
    dispositivo_critico = ""
    ambiente_critico = ""
    for ambiente in ambientes:
        for nombre_dispositivo, consumo in ambientes[ambiente]:
            if consumo > max_consumo:
                max_consumo = consumo
                dispositivo_critico = nombre_dispositivo
                ambiente_critico = ambiente
    if dispositivo_critico:
        print(f"El dispositivo que más energía consume es {dispositivo_critico} en {ambiente_critico} con {max_consumo} Watts")
    else:
        print("No se encontraron dispositivos activos.")

ambiente = cargar()
consumo_por_habitacion(ambiente)
dispositivo_critico(ambiente)