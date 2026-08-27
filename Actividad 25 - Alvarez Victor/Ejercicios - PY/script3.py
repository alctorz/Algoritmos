"""
3-  Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
    segundos) obtenidos en sus últimas 3 vueltas de clasificación.
    - La estructura de datos debe ser una lista general. Cada elemento de la lista será
      una sublista que contenga en el primer componente el nombre del piloto (cadena
      de caracteres) y en el segundo componente una tupla con sus 3 tiempos
      (flotantes).
    - Sugerencia de estructura interna si se cargara por asignación:
      pilotos = [ ["Franco", (78.5, 77.2, 79.1)], ["Lewis", (77.9, 78.1, 77.4)], ... ]
    Desarrollar las siguientes funciones:
    1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
       3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
    2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
       de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
    3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
       toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
       detallando a qué piloto le pertenece.
"""

def cargar():
   pilotos = []
   for x in range(4):
      nom = input(f"Ingrese el nombre del piloto {x+1}: ")
      vuelta1 = float(input("Ingrese el tiempo de la primera vuelta de la calificación del piloto: "))
      vuelta2 = float(input("Ingrese el tiempo de la segunda vuelta de la calificación del piloto: "))
      vuelta3 = float(input("Ingrese el tiempo de la tercera vuelta de la calificación del piloto: "))
      pilotos.append((nom, vuelta1, vuelta2, vuelta3))
   return pilotos

def calcular_promedios(pilotos):
   promedio = []
   for x in range(4):
      suma = pilotos[x][1] + pilotos[x][2] + pilotos[x][3]
      prom = suma / 3
      promedio.append(prom)

      print(f"El piloto con mejor promedio es {pilotos[x][0]} con {prom}")
   return promedio

def mejor_vuelta(pilotos):
   mejorv = 99
   for x in range(4):
      for z in range(3):
         if pilotos[x][z+1] < mejorv:
            mejorv = pilotos[x][z+1]
            pilot = pilotos[x][0]

   print (f"La mejor vuelta fue de {pilot} con {mejorv}") # type: ignore
   

pilotos = cargar()
calcular_promedios(pilotos)
mejor_vuelta(pilotos)