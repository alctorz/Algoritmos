"""
1- Crear un diccionario en Python que defina como clave el número de documento de
   una persona y como valor un string con su nombre.
   Desarrollar las siguientes funciones:
     1) Cargar por teclado los datos de 4 personas.
     2) Listado completo del diccionario.
     3) Consulta del nombre de una persona ingresando su número de documento.
"""

def cargar():
    personas = {}
    for x in range(4):
        dni = int(input(f"Ingrese el número de documento de la persona {x+1}: "))
        nom = input("Ingrese el nombre de la persona: ")
        personas[dni] = nom
    return personas

def imprimir(personas):
    print("Lista del diccionario: ")
    for dni in personas:
        print(dni, personas[dni])

def consulta(personas):
    documento = int(input("Ingrese el DNI a consultar: "))
    if documento in personas:
        print(f"La persona con el DNI es: {personas[documento]}")

personas = cargar()
imprimir(personas)
consulta(personas)