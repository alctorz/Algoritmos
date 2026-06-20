"""
2- Se desea saber la temperatura media trimestral de cuatro países. Para ello se
   tiene como dato las temperaturas medias mensuales de dichos países. Se debe
   ingresar el nombre del país y seguidamente las tres temperaturas medias
   mensuales.
   Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
   datos en memoria.

    ● Cargar por teclado los nombres de los países y las temperaturas
      medias mensuales.
    ● Imprimir los nombres de los países y las temperaturas medias
      mensuales de las mismas.
    ● Calcular la temperatura media trimestral de cada país.
    ● Imprimir los nombres de los países y las temperaturas medias
      trimestrales.
    ● Imprimir el nombre del país con la temperatura media trimestral
      mayor.
"""

paises = []
temperatura = []

for x in range(4):
  nom = input("Ingrese el nombre del país: ")
  paises.append(nom)
  for x in range(3):
    temp = int(input("Ingrese la temperatura media mensual: "))
    temperatura.append(temp)

for x in range(4):
  print(f"{paises[x]}: {temperatura[x*3]}, {temperatura[x*3+1]}, {temperatura[x*3+2]}")

print("Países y temperaturas medias trimestrales:")

tempt = []

for x in range(4):
  promedio = (temperatura[x*3] + temperatura[x*3+1] + temperatura[x*3+2]) / 3
  tempt.append(promedio)
  print(f"{paises[x]}: {promedio}")

print("Países y temperaturas medias mensuales:")

for x in range(4):
  for z in range(x + 1, 4):
    if tempt[x] < tempt[z]:
      aux = tempt[x]
      tempt[x] = tempt[z]
      tempt[z] = aux
      aux2 = paises[x]
      paises[x] = paises[z]
      paises[z] = aux2

print(f"El país con la temperatura media trimestral mayor es: {paises[z]} con una temperatura de {tempt[z]}")