document.addEventListener('DOMContentLoaded', function() {
  var miniaturas = document.querySelectorAll('.miniaturas img');
  var imagenGrande = document.getElementById('imagenGrande');
  var contenedorImagen = document.getElementById('contenedorImagen');

  miniaturas.forEach(function(miniatura) {
      miniatura.addEventListener('click', function() {
          var rutaImagen = this.src;
          imagenGrande.src = rutaImagen;
          contenedorImagen.style.display = 'flex';
          setTimeout(function() {
              contenedorImagen.style.opacity = '1';
              imagenGrande.style.transform = 'scale(1)';
          }, 50); // Retraso de 50 milisegundos para asegurar que la transición se aplique
      });
  });

  contenedorImagen.addEventListener('click', function(e) {
      if (e.target === this) {
          imagenGrande.style.transform = 'scale(0.7)';
          contenedorImagen.style.opacity = '0';
          setTimeout(function() {
              contenedorImagen.style.display = 'none';
          }, 500); // Retraso de 500 milisegundos para asegurar que la transición se aplique
      }
  });
});

