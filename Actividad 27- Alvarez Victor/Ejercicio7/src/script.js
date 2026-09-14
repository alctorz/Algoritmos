/*
7-  Confeccionar una página que muestre tres checkbox que permitan
    seleccionar los deportes que practica el usuario (Fútbol, Básquet, Tenis)
    Mostrar al presionar un botón los deportes que eligió.
*/

function Deportes(){
  let mensaje = 'Deportes seleccionados: ';
  let alguno = false;

  if (document.getElementById('futbol').checked) {
    mensaje += '-Fútbol.';
    alguno = true;
  }
  if (document.getElementById('basquet').checked) {
    mensaje += '-Básquet.';
    alguno = true;
  }
  if (document.getElementById('voleibol').checked) {
    mensaje += '-Voleibol.';
    alguno = true;
  }
  if (!alguno) {
    mensaje = 'No seleccionó ningún deporte.';
  }
  alert(mensaje);
}