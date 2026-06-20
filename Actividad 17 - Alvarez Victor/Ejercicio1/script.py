"""
1- Se tiene la siguiente lista:
   lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
   Imprimir la lista. Luego cambiar de elemento todos los enteros mayores a 50 del
   primer elemento de "lista". El resto de enteros menores a 50 deben encontrarse
   en una nueva posición dentro de la lista.
   Volver a imprimir la lista.
""" 

lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

print(f"La lista es: {lista}")

primer_elemento = []

for x in range(len(lista)):
  nueva_posicion = []
  for z in lista[x]:
    if z > 50:
      primer_elemento.append(z)        
    else:
      nueva_posicion.append(z)
    lista[x] = nueva_posicion

lista[0] = primer_elemento

print(f"La lista cambiada es: {lista}")