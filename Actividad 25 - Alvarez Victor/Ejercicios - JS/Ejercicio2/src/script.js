/*
2-  Para un sistema de radares de tránsito, se necesita registrar la ubicación geográfica de 4
    cámaras de control.
    - Almacenar en una lista las coordenadas de las 4 cámaras. Cada elemento de la
      lista debe ser una tupla de dos flotantes (latitud, longitud) ingresados por teclado.
    Desarrollar las siguientes funciones:
    1. Cargar coordenadas: Solicitar la latitud y la longitud de cada una de las 4
       cámaras para armar las tuplas y agregarlas a la lista.
    2. Listar posiciones: Recibir la lista e imprimir las coordenadas de todas las
       cámaras. Importante: Realizar el recorrido utilizando un bucle for que
       desempaquete la tupla directamente en las variables lat y lon en cada vuelta (sin
       utilizar índices numéricos como [0] o [1]).
    3. Filtrar hemisferio: Contar e informar cuántas de las cámaras se encuentran
       ubicadas en el hemisferio norte (latitud mayor a cero).
*/

function cargar(){
   camaras = []
   for(let x=0; x<4; x++){
      latitud = parseFloat(input(prompt("Ingrese la latitud de la cámara "+ x+1 +": ")))
      longitud = parseFloat(input(prompt("Ingrese la longitud de la cámara "+ x+1 +": ")))
   }
}

function listar_posiciones(camaras){
   for(let x=0; x<4; x++){
      for(let z=0; z<1; z++){
         console.log("La cámara ", x+1 ,"está ubicada en la latitud ", camaras[x][z],"y longitud ", camaras[x][z+1],".")
      }
   }
}

function filtrar_hemisferio(camaras){
   for(let x=0; x<4; x++){
      if(camaras[x][0] < 0){
         console.log("La cámara ", x+1,"está ubicada en el hemisferio norte");
      }
   }
}