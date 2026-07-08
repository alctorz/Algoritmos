"""
2- Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea
   el número de documento del alumno. Como valor almacenar una lista con
   componentes de tipo tupla donde almacenamos nombre de materia y su nota.
   Crear las siguientes funciones:
     1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las
        materias y sus notas)
     2) Listado de todos los alumnos con sus notas
     3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

def carga():
   diccionario = {}
   for x in range(3):
      dni = int(input(f"Ingrese el DNI del alumno {x + 1}: "))
      lista = []
      for z in range(1):
         nom = input("Ingrese el nombre de su materia: ")
         nota = int(input("Ingrese la nota que tuvo el alumno: "))
         lista.append((nom, nota))
      diccionario[dni] = lista    
   return diccionario

def imprimir(lista):
   print(lista)

def consulta(lista):
   valor = int(input("Ingrese el DNI a consultar: "))
   if valor in lista:
      print(lista[valor])

lista=carga()
imprimir(lista)
consulta(lista)