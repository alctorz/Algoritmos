/*
2-                          Detector de Transacciones Sospechosas (Parseo)
    Contexto: Un banco recibe un lote diario de movimientos en un único texto largo con el
              formato "ID:TIPO:MONTO", donde TIPO puede ser I (Ingreso) o E (Egreso), separados por
              comas.
    Consigna: Crear una función procesar_transacciones(cadena_texto) que reciba el texto de
              movimientos y realice el procesamiento completo.
    Requisitos:
        ● Parsear la cadena de texto separando cada registro.
        ● Calcular y retornar el balance total de la cuenta (Ingresos suman, Egresos restan).
        ● Generar y retornar una lista con los IDs de las transacciones consideradas
          "sospechosas". Una transacción es sospechosa si es un Egreso superior a
          $50.000.
          Ejemplo de Entrada: "TX101:I:120000, TX102:E:15000, TX103:E:85000,
                              TX104:I:3000" Salida Esperada:
            ● Balance final: $23.000
            ● Transacciones sospechosas: ['TX103'] 
*/

function procesar_transacciones(){
    let suma = 0;
    let lista1 = [];
    let lista2 = [];

    let num = parseInt(prompt("¿Cuántas veces desea ingresar datos?"));

    for (let x = 0; x < num; x++) {
        let id = prompt("Ingrese el ID del movimiento: ");
        let tipo = prompt("Ingrese el tipo (I/E): ");
        let monto = parseInt(prompt("Ingrese el monto: "));

        lista1.push(id + ":" + tipo + ":" + monto);

        if (tipo == "I") {
            suma = suma + monto;
        } else if (tipo == "E") {
            suma = suma - monto;
        }

        if (tipo == "E" && monto > 50000) {
            lista2.push(id);
        }
    }

    console.log(lista1);
    console.log("Balance final: $" + suma);
    console.log("Transacciones sospechosas: " + lista2);
}

procesar_transacciones();