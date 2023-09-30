document.addEventListener("DOMContentLoaded", function() {
  for (let i = 0; i < productos.length; i++) {
    const producto = productos[i];
    const nombreElemento = document.getElementById(`nombreProducto${i + 1}`);
    const descripcionElemento = document.getElementById(`descripcionProducto${i + 1}`);
    const precioElemento = document.getElementById(`precioProducto${i + 1}`);

    nombreElemento.textContent = producto.nombre;
    descripcionElemento.textContent = producto.descripcion;
    precioElemento.textContent = producto.precio;
  }
});
