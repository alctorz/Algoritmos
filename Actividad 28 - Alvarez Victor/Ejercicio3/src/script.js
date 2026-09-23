/*
3-  Solicitar que se ingrese el nombre y la clave de un usuario. Mostrar una ventana de
    alerta si en la clave se ingresan menos de 7 caracteres o más de 20 (capturar el evento
    onBlur)
*/

function contraseña(){
    if(document.getElementById("clave").value.length < 7){
        alert('La clave tiene menos de 7 carácteres.')
    }
    else if(document.getElementById("clave").value.length > 20){
        alert('La clave tiene más de 20 carácteres.')
    }
}