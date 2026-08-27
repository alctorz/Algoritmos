"""
1-  Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
    6 horas en una lista.
    Desarrollar las siguientes funciones:
    1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
              almacenarlas en una lista.
    2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
                          contenga en su primer componente el valor máximo y en el segundo el valor
                          mínimo.
    3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
                         variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
                         descriptivo.
"""

def carga():
    lista = []
    for x in range(6):
        temp = int(input(f"Ingrese la temperatura {x+1}: "))
        lista.append(temp)
    return lista

def procesar_extremos(lista):
    mayor = -999
    menor = 999
    for x in range(6):
        if lista[x] > mayor:
            mayor = lista[x]
        if lista[x] < menor:
            menor = lista[x]

    tupla = (mayor, menor)
    return tupla

def bloque_principal(tupla):
    maximo = tupla[0]
    minimo = tupla[1]

    print(f"El valor máximo es: {maximo}")
    print(f"El valor mínimo es: {minimo}")

lista = carga()
tupla = procesar_extremos(lista)
bloque_principal(tupla)