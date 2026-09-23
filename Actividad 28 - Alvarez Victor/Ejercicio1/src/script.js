/*
1-  Confeccionar una página que muestre dos objetos de la clase RADIO solicitando que
    seleccione si es mayor de 18 años o no. Al presionar un botón mostrar un alert
    indicando si puede ingresar al sitio o no.
*/

function seleccionarEdad(){
    if (document.getElementById('radio1').checked){
        alert('Eres mayor de edad.')
    }
    if (document.getElementById('radio2').checked){
        alert('Eres menor de edad, no puede ingresar al sitio.')
    }
}