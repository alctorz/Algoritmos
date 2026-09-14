/*
6-  Confeccionar una página que permita tomar un examen múltiple choice.
    Se debe mostrar una pregunta y seguidamente un objeto SELECT con
    las respuestas posibles. Al presionar un botón mostrar la cantidad de
    respuestas correctas e incorrectas (Disponer 4 preguntas y sus
    respectivos controles SELECT)
*/

function calcularResultados(){
    let respuestasCorrectas = 0;
    let respuestasIncorrectas = 0;

    const respuesta1 = document.getElementById("respuesta1").value;
    const respuesta2 = document.getElementById("respuesta2").value;
    const respuesta3 = document.getElementById("respuesta3").value;
    const respuesta4 = document.getElementById("respuesta4").value;

    if (respuesta1 === "b") {
        respuestasCorrectas++;
    } else {
        respuestasIncorrectas++;
    }

    if (respuesta2 === "a") {
        respuestasCorrectas++;
    }
    else {
        respuestasIncorrectas++;
    }

    if (respuesta3 === "c") {
        respuestasCorrectas++;
    }
    else {
        respuestasIncorrectas++;
    }

    if (respuesta4 === "d") {
        respuestasCorrectas++;
    }
    else {
        respuestasIncorrectas++;
    }

    const resultado = document.getElementById("resultado");
    resultado.textContent = `Respuestas correctas: ${respuestasCorrectas}, Respuestas incorrectas: ${respuestasIncorrectas}`;
}

