"""
3- Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
   carrera de 100 metros. El programa debe cargar los datos en dos vectores
   paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
   atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
   promedio.
"""

atletas = []
tiempos = []

for x in range(5):
    nombre = input("Ingrese el nombre del atleta: ")
    tiempo = int(input("Ingrese el tiempo del atleta en segundos: "))
    atletas.append(nombre)
    tiempos.append(tiempo)

promedio = sum(tiempos) / len(tiempos)
mejor = min(tiempos)
peor = max(tiempos)
print(f"El promedio de los tiempos es: {promedio} segundos.")

for x in range(5):
    if tiempos[x] == mejor:
        print(f"El atleta con el mejor tiempo es: {atletas[x]} con un tiempo de {tiempos[x]} segundos.")
    if tiempos[x] == peor:
        print(f"El atleta con el peor tiempo es: {atletas[x]} con un tiempo de {tiempos[x]} segundos.")
    if tiempos[x] < promedio:
        print(f"El atleta {atletas[x]} superó el promedio con un tiempo de {tiempos[x]} segundos.")