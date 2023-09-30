function agregarALaOperacion(valor) {
    document.getElementById('resultado').value += valor;
  }

  function calcularResultado() {
    try {
      let resultado = eval(document.getElementById('resultado').value);
      if (isNaN(resultado)) {
        throw new Error('Operación inválida');
      }
      document.getElementById('resultado').value = resultado;
    } catch (error) {
      document.getElementById('resultado').value = 'Error';
    }
  }

  function limpiarResultado() {
    document.getElementById('resultado').value = '';
  }