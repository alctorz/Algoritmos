/*
5-                      Control de Temperatura
    Diseñar una página con un campo de texto para ingresar una temperatura y un botón
    “Verificar”.
    Cuando el usuario haga clic:
    - Si la temperatura es menor a 10, mostrar en el documento el mensaje “Hace
      frío” en azul.
    - Si está entre 10 y 25, mostrar “Clima agradable” en verde.
    - Si es mayor a 25, mostrar “Hace calor” en rojo.
      Además, cada verificación debe registrarse en consola con la fecha y hora
      exacta (usando Date()).
*/

let temp = document.querySelector("#inputTemp")
let verificarTemp = document.querySelector("#btnVerificarTemp")
let resultadoTemp = document.querySelector("#resultadoTemp")

verificarTemp.addEventListener("click", function(){
  let temp = parseFloat(temp.value);
  if (isNaN(temp)){
    resultadoTemp.textContent = "Por favor ingresa un número válido";
    resultadoTemp.style.color = "orange";
    return;
  }

  let mensaje, color
  if (temp < 10){
    mensaje = "Hace frío";
    color = "blue";
  }
  else if (temp <= 25){
    mensaje = "Clima agradable";
    color = "green";
  }
  else{
    mensaje = "Hace calor";
    color = "red";
  }

  resultadoTemp.textContent = mensaje;
  resultadoTemp.style.color = color;

  console.log(`Verificación de temperatura (${temp}°C): ${mensaje} - ${new Date()}`);
});