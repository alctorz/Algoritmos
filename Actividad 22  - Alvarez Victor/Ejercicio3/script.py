"""
3- Un equipo de seguridad informática registra las direcciones IP de servidores
   sospechosos que intentan acceder de forma no autorizada al sistema.
   - Crear un diccionario donde la Clave sea la dirección IP (cadena de
     caracteres, ej: "192.168.1.50") y el Valor sea una tupla que contenga:
     (nombre_del_dispositivo, cantidad_intentos_fallidos).
   Desarrollar las siguientes funciones:
   1. Cargar registro: Solicitar por teclado la carga de 4 direcciones IP
      sospechosas junto a los datos del dispositivo y sus intentos fallidos.
   2. Listar amenazas: Imprimir la lista de todas las IPs registradas indicando
      qué dispositivo es y cuántos intentos realizó.
   3. Filtrar Bloqueos: Recorrer el diccionario e informar las direcciones IP que
      deben ser bloqueadas inmediatamente por seguridad (aquellas con más de
      5 intentos fallidos).
"""

def cargar():
    registro = {}
    for x in range(4):
        ip = int(input("Ingrese la dirección IP sospechosa: "))
        nombreD = input(f"Ingrese el nombre del dispositivo {x + 1}: ")
        intentosF = int(input("Ingrese la cantidad de intentos fallidos: "))
        registro[ip] = (nombreD, intentosF)
    return registro

def listado(registro):
    print("Listado de amenazas registradas: ")
    for ip in registro:
        print(ip, registro[ip])

def filtrar(registro):
    print("Direcciones IP que deben ser bloqueadas: ")
    for ip in registro:
        nombreD, intentosF = registro[ip]
        if intentosF > 5:
            print(f"IP: {ip}, Dispositivo: {nombreD}, Intentos fallidos: {intentosF}")

registro = cargar()
listado(registro)
filtrar(registro) 