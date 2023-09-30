function esPrimo(numero) {
    if (numero <= 1) {
      throw new Error("El número debe ser mayor que 1");
    }
    for (let i = 2; i < numero; i++) {
      if (numero % i === 0) {
        throw new Error("El número no es primo");
      }
    }
    return true;
  }
  
  function verificarPrimo() {
    let numero = document.getElementById("numero").value;
  
    // Verificar si el valor es un número
    if (!isNaN(numero) && numero !== "") {
      numero = parseInt(numero);
      let messageList = document.getElementById("message-list");
  
      try {
        esPrimo(numero);
        messageList.innerHTML += `<li class="sent">El número ${numero} es primo.</li>`;
      } catch (error) {
        messageList.innerHTML += `<li class="received">${error.message}</li>`;
      }
  
      // Limpiar el input después de enviar el mensaje
      document.getElementById("numero").value = "";
    }
  }
  