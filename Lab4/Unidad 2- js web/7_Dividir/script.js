function agregarALaOperacion(valor) {
    document.getElementById('resultado').value += valor;
  }
  
  function calcularResultado() {
    try {
      let operacion = document.getElementById('resultado').value;
      if (operacion.includes('/0')) {
        throw new Error('No se puede dividir por 0');
      }
      
      let resultado = eval(operacion);
      if (isNaN(resultado)) {
        throw new Error('Operación inválida');
      }
      
      document.getElementById('resultado').value = resultado;
    } catch (error) {
      document.getElementById('resultado').value = 'Error';
      if (error.message === 'No se puede dividir por 0') {
        alert('No se puede dividir por 0');
      }
    }
  }
  
  function limpiarResultado() {
    document.getElementById('resultado').value = '';
  }
  