"""
3- Confeccionar un programa que permita:
    1) Cargar una lista de 10 elementos enteros.
    2) Generar dos listas a partir de la primera. En una guardar los valores
       positivos y en otra los negativos.
    3) Imprimir las dos listas generadas.
"""

def ejercicio(lista1, lista2, lista3):
    for x in range (10):
        valor1 = int(input("Ingrese un numero entero: "))
        lista1.append(valor1)
    for x in range (10):
        if lista1[x] > 0:
            lista2.append(lista1[x])
        elif lista1[x] < 0:
            lista3.append(lista1[x])

    print(f"La lista original: {lista1}")
    print(f"La lista de núumeros positivos es: {lista2}")
    print(f"La lista de números negativos es: {lista3}")

numeros=[]
listaPos=[]
listaNeg=[]
ejercicio(numeros, listaPos, listaNeg)