"""
1- Confeccionar un programa con las siguientes funciones:
   1)Cargar una lista de 5 enteros.
   2)Retornar el mayor y menor valor de la lista mediante una tupla.
     Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

def cargar(Lista):
    for x in range (5):
        nom = int(input("ingrese un numero entero: "))
        Lista.append(nom)
    return Lista

def numeroMayYMen(Lista):
    elementomen = 0
    elementomay = 99999
    for x in range (5):
        if elementomen < Lista[x]:
            elementomen = Lista[x]
        if elementomay > Lista[x]:
            elementomay = Lista[x]

    numeros = elementomay, elementomen
    return numeros

lista=[]

print(cargar(lista))
lista=numeroMayYMen(lista)
print(f"El número más pequeño y el más grande son:{lista}")