function sumarLista(lista) {
    let suma = 0;

    for (let i = 0; i < lista.length; i++) {
        suma += lista[i];
    }

    return suma;
}
let numeros = [1, 2, 3, 4, 5];
let resultado = sumarLista(numeros);
console.log("Resultado: ", resultado);
