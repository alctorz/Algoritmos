/*
3-  Un equipo de Fórmula 1 registra los nombres de sus 4 pilotos junto con los tiempos (en
    segundos) obtenidos en sus últimas 3 vueltas de clasificación.
    - La estructura de datos debe ser una lista general. Cada elemento de la lista será
      una sublista que contenga en el primer componente el nombre del piloto (cadena
      de caracteres) y en el segundo componente una tupla con sus 3 tiempos
      (flotantes).
    - Sugerencia de estructura interna si se cargara por asignación:
      pilotos = [ ["Franco", (78.5, 77.2, 79.1)], ["Lewis", (77.9, 78.1, 77.4)], ... ]
    Desarrollar las siguientes funciones:
    1. Cargar pilotos: Solicitar por teclado el nombre de cada uno de los 4 pilotos y sus
       3 mejores tiempos para estructurar la lista y las tuplas correspondientes.
    2. Calcular Promedios: Recorrer la estructura de datos, calcular el tiempo promedio
       de cada piloto en sus 3 vueltas e imprimir su nombre junto a dicho promedio.
    3. Mejor Vuelta: Recorrer la estructura para buscar y mostrar la vuelta más rápida de
       toda la clasificación (el tiempo individual más bajo dentro de cualquier tupla),
       detallando a qué piloto le pertenece.
*/

function cargar(){
   pilotos = []
   for(let x=0; x<4; x++){
      nom = prompt("Ingrese el nombre del piloto ", x+1 ,": ")
      vuelta1 = parseFloat(prompt("Ingrese la primera vuelta del piloto: "))
      vuelta2 = parseFloat(prompt("Ingrese la segunda vuelta del piloto: "))
      vuelta3 = parseFloat(prompt("Ingrese la tercera vuelta del piloto: "))
      pilotos.push((nom, vuelta1, vuelta2, vuelta3))
   return pilotos
   }
}

function calcular_promedios(pilotos){
   promedio = []
   for(let x = 0; x<4; x++){
      suma = pilotos[x][1] + pilotos[x][2] + pilotos[x][3]
      prom = suma / 3

      print("El piloto con mejor promedio es ", piloto[x][0], "con ", suma, ".");
   }
   return promedio
}

function mejor_vuelta(pilotos){
   mejorv = 99
   for(let x = 0; x<4; x++){
      for(let z = 0; x<3; x++){
         if(pilotos[x][z+1] < mejorv){
            mejorv = pilotos[x][z+1]
            pilot = pilotos[x][0]
         }
      }
   }
   print("El piloto con mejor vuelta es ", mejorv ,"con ", pilot ,".")
}

cargar()
calcular_promedios(pilotos)
mejor_vuelta(pilotos)