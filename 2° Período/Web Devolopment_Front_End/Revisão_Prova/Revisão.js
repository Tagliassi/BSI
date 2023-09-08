// Conceitos de P.O.O

class MeuObjeto {
    constructor() {
        this.propriedade1 = "Valor da Propriedade 1";
        this.propriedade2 = 42;
    }

    metodo1() {
        console.log("Este é um método do objeto.");
    }
}

// Instanciar um objeto usando a classe
const meuObjeto = new MeuObjeto();

// Acessar propriedades e chamar métodos
console.log(meuObjeto.propriedade1);
console.log(meuObjeto.propriedade2);
meuObjeto.metodo1();

// Conceitos de Variáveis

var a = 1;
let b = 2;
const c = 3;

if (true) {
    var a = 10; // Escopo global
    let b = 20; // Escopo de bloco
    const c = 30; // Escopo de bloco
}

console.log(a); // 10 (variável global)
console.log(b); // 2 (variável de bloco)
console.log(c); // 3 (variável de bloco)

// Tentando acessar variáveis antes de sua declaração
console.log(d); // undefined (hoisting com var)
console.log(e); // ReferenceError: e is not defined (let e const não são hoisted)

var d = 5;
let e = 6;

// Conceito de estruturas condicionais (Guard Clauses)

function dividir(a, b) {
    if (b === 0) {
        console.error("Divisão por zero não é permitida.");
        return;
    }
    return a / b;
}

// Conceitos de loop (do while)

let numero = 0;
do {
    console.log(numero);
    numero++;
} while (numero < 5);

// Conceitos de loop (for in)

const carro = {
    marca: "Toyota",
    modelo: "Corolla",
    ano: 2021
};

for (let chave in carro) {
    console.log(chave + ": " + carro[chave]);
}



