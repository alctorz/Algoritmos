"""
4- Un observatorio astronómico registra los descubrimientos de nuevos planetas
   fuera del sistema solar.
   - Diseñar un diccionario donde la Clave sea el nombre científico del
     exoplaneta (ej: "Kepler-22b") y el Valor sea una tupla con sus datos:
     (distancia_anios_luz, tipo_de_atmosfera, es_habitable_booleano).
   Desarrollar las siguientes funciones:
   1. Cargar catálogo: Registrar por teclado la información de 4 exoplanetas
      descubiertos.
   2. Buscar exoplaneta: Permitir al usuario ingresar el nombre de un
      exoplaneta por teclado. Si el exoplaneta se encuentra en el diccionario
      (utilizando el operador in), mostrar todos sus detalles físicos y si reúne
      condiciones de habitabilidad. De lo contrario, mostrar un cartel indicando:
      "El exoplaneta no figura en el catálogo actual".
   3. Reportar Habitables: Mostrar en pantalla únicamente los nombres de los
      exoplanetas cargados que fueron marcados como habitables.
"""

def cargar():
    catalogo = {}
    for x in range(4):
        nombre = input(f"Ingrese el nombre científico del exoplaneta {x + 1}: ")
        distancia = int(input("Ingrese la distancia en años luz: "))
        tipo_atmosfera = input("Ingrese el tipo de atmósfera: ")
        habitable = input("¿Es habitable? (si/no): ")
        catalogo[nombre] = (distancia, tipo_atmosfera, habitable)
    return catalogo

def buscar(catalogo):
    nombre = input("Ingrese el nombre del exoplaneta a buscar: ")
    if nombre in catalogo:
        distancia, tipo_atmosfera, habitable = catalogo[nombre]
        print(f"Exoplaneta: {nombre}")
        print(f"Distancia: {distancia} años luz")
        print(f"Tipo de atmósfera: {tipo_atmosfera}")
        print(f"¿Es habitable?: {habitable}")
    else:
        print("El exoplaneta no figura en el catálogo actual.")

def reportar(catalogo):
    print("Exoplanetas habitables:")
    for nombre in catalogo:
        distancia, tipo_atmosfera, habitable = catalogo[nombre]
        if habitable == "si":
            print(nombre)

catalogo = cargar()
buscar(catalogo)
reportar(catalogo)