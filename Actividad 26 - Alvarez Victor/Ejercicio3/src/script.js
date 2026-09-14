/*
3-                      Simulador de Votación en Línea
    Plantear una página con 3 botones, cada uno representando un candidato distinto.
    Al hacer clic en uno de los botones, se deberá aumentar el contador de votos de ese
    candidato y mostrar el total actualizado en pantalla.
    Además:
    - El sistema debe mostrar en consola quién va ganando cada vez que se registra
      un voto.
    - Si hay un empate, debe mostrar el mensaje “Hay un empate”.
*/

let votos = { A: 0, B: 0, C: 0 }

let btnsVoto = document.querySelectorAll(".boton-voto")

let contadores = document.querySelectorAll(".contador")

function actualizarContadores(){
  contadores.forEach(function(contador){
    let candidato = contador.dataset.candidato
    contador.textContent = votos[candidato];
  });
}

function verificarGanador(){
  let maxVotos = Math.max(votos.A, votos.B, votos.C)
  let ganadores = Object.keys(votos).filter((c) => votos[c] === maxVotos)

  if (ganadores.length > 1){
    console.log("Hay un empate.");
  } 
  else{
    console.log(`Va ganando el Candidato ${ganadores[0]} con ${maxVotos} voto(s)`);
  }
}

btnsVoto.forEach(function(boton){
  boton.addEventListener("click", function(){
    let candidato = boton.dataset.candidato
    votos[candidato]++;
    actualizarContadores();
    verificarGanador();
  });
});