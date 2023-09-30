

let esconderTexto_btn = document.getElementById('esconderTexto_btn');

let esconderTexto = document.getElementById('esconderTexto');

esconderTexto_btn.addEventListener('click', toggleText);

function toggleText(){
    esconderTexto.classList.toggle("mostrar");

    if(esconderTexto.classList.contains("mostrar")){
        esconderTexto_btn.innerHTML = 'Ocultar'
    }else{
        esconderTexto_btn.innerHTML = 'Saludar'
    }
}
