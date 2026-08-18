"""
2-  En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
    para realizar misiones cooperativas.
    - Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej:
      "DragonesDeFuego") y el Valor sea una lista de cadenas con los nombres de
      los jugadores (nicknames) que lo integran.
    Desarrollar las siguientes funciones:
    1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
       preguntar cuántos integrantes posee para cargar sus respectivos nombres de
       usuario en la lista interna.
    2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
       de miembros que posee cada uno.
    3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
       gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
       "Solitario" (no pertenece a ningún clan).
"""

def registrar():
    gremios = {}
    for x in range(3):
        gremio = input(f"Ingrese el nombre del gremio {x + 1}: ")
        integrantes = int(input(f"Ingrese la cantidad de integrantes en {gremio}: "))
        jugadores = []
        for z in range(integrantes):
            jugador = input(f"Ingrese el nombre del jugador {z + 1} en {gremio}: ")
            jugadores.append(jugador)
        gremios[gremio] = jugadores
    return gremios

def listar(gremios):
    for gremio in gremios:
        cantidad = len(gremios[gremio])
        print(f"Gremio: {gremio}, Cantidad de miembros: {cantidad}")

def buscar_jugador(gremios):
    jugador = input("Ingrese el nombre del jugador a buscar: ")
    for gremio in gremios:
        integrantes = gremios[gremio]
        if jugador in integrantes:
            print(f"El jugador {jugador} pertenece al gremio {gremio}")
            return
    print(f"El jugador {jugador} es solitario (no pertenece a ningún clan)")

gremio = registrar()
listar(gremio)
buscar_jugador(gremio)    