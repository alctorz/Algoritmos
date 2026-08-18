"""
1-  Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes de
    dióxido de carbono (CO2) en diferentes puntos geográficos.
    - Crear un diccionario donde la Clave sea el nombre del barrio o estación de
      monitoreo (ej: "San Telmo") y el Valor sea una lista de flotantes que represente
      las últimas 3 lecturas de contaminación tomadas en el día.
    Desarrollar las siguientes funciones:
    1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
       una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
    2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada
       barrio.
    3. Alerta ambiental: Mostrar en pantalla una alerta roja de "Protocolo de
       Emergencia" únicamente para las estaciones cuyo promedio de contaminación
       supere las 400 ppm.
"""

def cargar():
    sensores = {}
    for x in range(3):
        barrio = input(f"Ingrese el nombre del barrio o estación de monitoreo {x + 1}: ")
        lecturas = []
        for z in range(3):
            lectura = float(input(f"Ingrese la lectura {z + 1} de CO2 (ppm) para {barrio}: "))
            lecturas.append(lectura)
        sensores[barrio] = lecturas
    return sensores

def reportar(sensores):
    for barrio in sensores:
        lecturas = sensores[barrio]
        promedio = sum(lecturas) / len(lecturas)
        print(f"El promedio de contaminación en {barrio} es: {promedio} ppm")

def alerta(sensores):
    for barrio in sensores:
        lecturas = sensores[barrio]
        promedio = sum(lecturas) / len(lecturas)
        if promedio > 400:
            print(f"Alerta roja: Protocolo de Emergencia en {barrio}")

sensores = cargar()
reportar(sensores)
alerta(sensores)