/*
4-  Un comercio de tecnología necesita administrar el stock de sus 5 componentes clave de
    hardware.
    - Crear una lista donde cada elemento sea una tupla de tres elementos que
      represente: (nombre_articulo, precio, stock).
    Desarrollar las siguientes funciones:
    1. Cargar inventario: Ingresar por teclado los datos de los 5 componentes para
       armar las tuplas correspondientes.
    2. Imprimir listado: Mostrar por pantalla los nombres, precios y stock de todos los
       artículos desempaquetando la tupla de manera directa en el bucle for.
    3. Valor del Inventario: Calcular e informar el valor total de la mercadería en el local
       (sumando el resultado de precio * stock de cada uno de los componentes).
    4. Alerta de Reposición: Imprimir el nombre de todos aquellos artículos cuyo stock
       sea menor o igual a 10 unidades para emitir un aviso de compra urgente.
*/

function cargar(){
   lista = []
   for(let x = 0; x<5; x++){
      nombre_articulo = prompt("Ingrese el nombre del artículo ", x + 1 ,": ")
      precio = parseInt(prompt("Ingrese el precio del artículo ", x + 1 ,": "))
      stock = parseInt(prompt("Ingrese el stock del artículo ", x + 1 ,": "))
      lista.push((nombre_articulo, precio, stock))
   }
   return lista
}

function imprimir_listado(lista){
   print("Listado de artículos:")
   for(let x = 0; x < lista.length; x++){
      let [nombre_articulo, precio, stock] = lista[x]
      print("Nombre: ", nombre_articulo, "Precio: ", precio, "Stock: ", stock);
   }
}

function valor_inventario(lista){
   total = 0;
   for(let x = 0; x < lista.length; x++){
      let [nombre_articulo, precio, stock] = lista[x]
      total += precio * stock
   }
   print("Valor total del inventario: ", total);
}

function alerta_reposicion(lista){
   print("Artículos con stock menor o igual a 10 unidades:")
   for(let x = 0; x < lista.length; x++){
      let [nombre_articulo, precio, stock] = lista[x]
      if(stock <= 10){
         print("Nombre: ", nombre_articulo, "Stock: ", stock);
      }
   }
}

let lista = cargar()
imprimir_listado(lista)