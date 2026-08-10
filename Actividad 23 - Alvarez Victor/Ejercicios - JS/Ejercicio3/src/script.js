/*
3- Tabla de Posiciones con Desempate (Listas Paralelas)
    Contexto: Se está organizando un torneo deportivo y se necesita generar la tabla de
              posiciones a partir de tres listas paralelas sincronizadas por índice: equipos, puntos y
              diferencia_gol.
    Consigna: Diseñar un algoritmo de ordenamiento que reorganice las tres listas de mayor a
              menor según el desempeño de cada equipo.
    Requisitos:
        ● Criterio Principal: Mayor cantidad de puntos.
        ● Criterio de Desempate: Si dos o más equipos empatan en puntos, la posición se
          define por el equipo que tenga la mayor diferencia de gol.
        ● Mantener la sincronización perfecta entre las tres listas al realizar los intercambios.
          Ejemplo de Entrada: equipos = ["Boca", "River", "Racing"] puntos = [12, 15, 12]
          diferencia_gol = [8, 5, 10] Salida Esperada: 1° River (15 pts), 2° Racing (12 pts,
          DG 10), 3° Boca (12 pts, DG 8).
*/

function ingresar(equipos, puntos, diferencia_gol){
    for(let x=0; x<3; x++){
        let equipo= prompt("Ingrese el nombre del equipo: ");
        equipos.push(equipo);
        let punto= parseInt(prompt("Ingrese los puntos del equipo : "));
        puntos.push(punto);
        let dif=parseInt(prompt("Ingrese la diferencia de goles del equipo: "));
        diferencia_gol.push(dif);
    }
}

function ordenar_tabla(equipos, puntos, diferencia_gol){
    for(let x=0; x<equipos.length; x++){
        for(let z=0; z<equipos.length; z++){
            if(puntos[z] < puntos[z + 1]){
                aux = puntos[z] 
                puntos[z] = puntos[z + 1] 
                puntos[z + 1] = aux
                aux = equipos[z] 
                equipos[z] = equipos[z + 1] 
                equipos[z + 1] = aux
                aux = diferencia_gol[z] 
                diferencia_gol[z] = diferencia_gol[z + 1] 
                diferencia_gol[z + 1] = aux
            }
            
            else if(puntos[z] == puntos[z + 1]){
                if(diferencia_gol[z] < diferencia_gol[z + 1]){
                aux = puntos[z] 
                puntos[z] = puntos[z + 1] 
                puntos[z + 1] = aux                    
                aux = equipos[z] 
                equipos[z] = equipos[z + 1] 
                equipos[z + 1] = aux
                aux = diferencia_gol[z] 
                diferencia_gol[z] = diferencia_gol[z + 1] 
                diferencia_gol[z + 1] = aux
                }
            }
        }
    }
}

let equipos = [];
let puntos = [];
let diferencia_gol = [];

ingresar(equipos, puntos, diferencia_gol);
ordenar_tabla(equipos, puntos, diferencia_gol);

console.log("Tabla de posiciones:");

for(let x=0; x<equipos.length; x++){
    console.log(x + 1, " ", equipos[x], " ", puntos[x], "pts  DG", diferencia_gol[x]);
}