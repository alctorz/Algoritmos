/*
4-                  Lista de Compras Dinámica
    Confeccionar una página con un campo de texto y un botón “Agregar”.
    Cada vez que se presione el botón, el producto ingresado en el campo debe añadirse
    a una lista (<ul>).
    Además:
    - La lista debe permitir eliminar un producto haciendo clic sobre él.
    - En consola debe mostrarse en todo momento la cantidad de productos
      actuales en la lista.
*/

let producto = document.getElementById("inputProducto")
let agregarProducto = document.getElementById("btnAgregarProducto")
let compras = document.getElementById("listaCompras")

function cantProductos(){
  console.log("Cantidad de productos en la lista:");
  console.log(compras.children.length);
}

agregarProducto.addEventListener("click", function(){
  let texto = producto.value.trim()
  if (texto === "") return;

  let li = document.createElement("li")
  li.textContent = texto;
  compras.appendChild(li);

  producto.value = "";
  cantProductos();
})


compras.addEventListener("click", function(event){
  if (event.target.tagName === "LI"){
    event.target.remove();
    cantProductos();
  }
})