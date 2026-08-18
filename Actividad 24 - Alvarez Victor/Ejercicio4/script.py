"""
4-  Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
    y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
    - Diseñar un diccionario donde la Clave sea el identificador único del dron (ej:
      &quot;DRON-01&quot;) y el Valor sea una lista de tuplas que almacene las coordenadas de
      las paradas programadas: [(latitud, longitud)].
    Desarrollar las siguientes funciones:
    1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
       uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas
       geográficas.
    2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
       de coordenadas asociadas.
    3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
       cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad
       de elementos).
"""

def cargar():
    drones = {}
    for x in range(3):
        id = input(f"Ingrese el identificador único del dron {x + 1}: ")
        paradas = []
        cantidad_paradas = int(input(f"Ingrese la cantidad de paradas para {id}: "))
        for z in range(cantidad_paradas):
            latitud = float(input(f"Ingrese la latitud de la parada {z + 1} para {id}: "))
            longitud = float(input(f"Ingrese la longitud de la parada {z + 1} para {id}: "))
            paradas.append((latitud, longitud))
        drones[id] = paradas
    return drones

def imprimir_rutas(drones):
    for id in drones:
        paradas = drones[id]
        print(f"Dron: {id}, Paradas: {paradas}")

def ruta_mas_larga(drones):
    max_paradas = 0
    dron_mas_largo = ""
    for id in drones:
        cantidad_paradas = len(drones[id])
        if cantidad_paradas > max_paradas:
            max_paradas = cantidad_paradas
            dron_mas_largo = id
    if dron_mas_largo:
        print(f"El dron con la ruta más larga es {dron_mas_largo} con {max_paradas} paradas")
    else:
        print("No se encontraron drones con rutas registradas.")

drones = cargar()
imprimir_rutas(drones)
ruta_mas_larga(drones)