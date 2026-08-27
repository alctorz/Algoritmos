"""
2-  Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
    cámaras de control.
    - Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
      lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
    Desarrollar las siguientes funciones:
    1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
       cámaras para armar las tuplas y agregarlas a la lista.
    2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
       cámaras. Importante: Realizar el recorrido utilizando un bucle for que
       desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
       utilizar índices numéricos como [0] o [1]).
    3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
       ubicadas en el hemisferio norte (latitud mayor a cero).
"""

def cargar():
    camaras = []
    for x in range(4):
        latitud = float(input(f"Ingrese la latitud de la cámara {x+1}: "))
        longitud = float(input(f"Ingrese la longitud de la cámara {x+1}: "))

def listar(camaras):
    for x in range(4):
        for z in range(1):
            print(f"La cámara {x+1} está ubicada en la latitud {camaras[x][z]} y longitud {camaras[x][z+1]}.")

def filtrar_hemisferio(camaras):
    for x in range(4):
        if camaras[x][0] < 0:
            print(f"La cámara {x+1} se encuentra en el hemisferio norte.")

camaras = cargar()
listar(camaras)
filtrar_hemisferio(camaras)