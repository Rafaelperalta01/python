function validarFormulario() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var alertasAnteriores = document.getElementsByClassName("alerta");
    while (alertasAnteriores.length > 0) {
        alertasAnteriores[0].parentNode.removeChild(alertasAnteriores[0]);
    }
    if (email === "" || password === "" || nombre === "") {
        var alerta = document.createElement("div");
        alerta.className = "alerta";
        alerta.innerText = "Por favor, completa los campos.";
        alert("Completa los campos por favor.")
        
        
        var formulario = document.getElementById("loginForm");
        formulario.parentNode.insertBefore(alerta, formulario);

        return false;
    }
    cerrarAlerta()
    return true;
}

function actualizarFondo(e) {
    var x = e.clientX / window.innerWidth - 0.5;
    var y = e.clientY / window.innerHeight - 0.5;
    var movimientoX = -x * 30;
    var movimientoY = -y * 30; 
    document.body.style.backgroundPosition = movimientoX + 'px ' + movimientoY + 'px';
}

document.addEventListener('mousemove', function(e) {
    requestAnimationFrame(function() {
        actualizarFondo(e);
    });
});