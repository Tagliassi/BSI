// Tipos de Dados

//Symbol => Um tipo de dado cujas instâncias são únicas e imutáveis
//Object => Coleções de propriedades

// Conversão de dados (implícita)

const numero1 = 42;
const texto = "5";
const resultado = numero1 + texto; // O JavaScript converte 'numero' para string e realiza a concatenação
console.log(resultado); // Saída: "425"

// Conversão de dados (explícita) parseInt, parseFloat...

const texto1 = "42";
const numero2 = parseInt(texto);
console.log(numero2); // Saída: 42

const texto2 = "42";
const numero3 = Number(texto);
console.log(numero3); // Saída: 42

const valor = "algum valor";
const booleano = Boolean(valor);
console.log(booleano); // Saída: true (a menos que 'valor' seja uma string vazia ou 'null' ou 'undefined')


// Operadores

x = 3
x = x++ // 3 depois 3+1
x = ++x // 3+1

+"3" // converte para number
+true // converte para number, ou seja, 1 = true e 0 = false

const fruits = ['banana', 'morango', 'melancia']

0 in fruits // return true, especificar o index e propriedades de arrays.

// instanceof é utilizado para ver se um objeto é uma instancia de uma classe ou outro objeto;

// Conceitos de Arrays

const letters = ['a','b','c'];
letters.push('d');
console.log(letters); // ['a', 'b', 'c', 'd']
console.log(letters.length); // 4
console.log(Object.keys(letters)); // ['0', '1', '2', '3']
console.log(letters[3]) // 'd'
letters.length = 2; // ['0', '1']

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

// Conceitos de Variáveis (Hoisting)

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

// Conceitos de Variáveis (Const)

const pi = 3.14159;
pi = 3; // Isso gerará um erro, pois você não pode reatribuir um valor a uma variável constante

const numbers = [1, 2, 3];
numbers.push(4); // Isso é permitido, pois estamos modificando o array, não reatribuindo 'numbers'


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

// Conceitos de loop (for of)

const frutas = ["maçã", "banana", "laranja"];
for (let fruta of frutas) {
    console.log(fruta);
}

// Conceitos de loop (for each)

const numeros = [1, 2, 3, 4, 5];

numeros.forEach(function(numero) {
    console.log(numero);
});


// Conceitos de Funções

function square(number){
   return number * number;
}

// Conceitos de Funções (Expressões ou funções anônimas)

//soma é uma variável que contém uma função anônima.
const soma = function(a, b) {
    return a + b;
};

//multiplicacao é uma variável que armazena uma função de flecha.
const multiplicacao = (a, b) => a * b;

const dobrar = function(numero) {
    return numero * 2;
};
  
const resultado1 = [1, 2, 3].map(dobrar); // Passando a função 'dobrar' como argumento para 'map'

(function() {
console.log("Isso é uma IIFE (Immediately Invoked Function Expression).");
})();

// Conceitos de Funções (inner functions)

function exterior() {
    const mensagem = "Hello, ";
  
    function interior(nome) {
      console.log(mensagem + nome);
    }
  
    return interior;
}
  
const saudacao = exterior();
saudacao("Alice"); // Saída: "Hello, Alice"

// Conceitos de Funções (hoisting)

hoistingExample(); // Isso funciona devido ao hoisting da função

function hoistingExample() {
  console.log("Hoisting de função!");
}


hoistingExample2(); // Isso resultará em um erro porque 'hoistingExample' não foi declarada ainda

const hoistingExample2 = function() {
  console.log("Hoisting de função!");
};

// Exercises

//Bhaskara

// const pol_2_grau = a*(x*x) + b*x + c
// const raizes = (-b +||- raiz(delta)) / 2*a
// const delta = b**2 - 4*a*c

function bhaskara(a,b,c){
    function delta(a,b,c){
        return b**2 - 4*a*c;
    }

    let d = delta(a,b,c);

    if (d < 0) {
        console.log("Duas raízes imaginárias")
    }
    else if (d === 0) {
        let r = -b / 2*a
        console.log(`Duas raízes iguais de valor ${r}`)
    }
    else{
        let r1 = (-b + Math.sqrt(d)/2*a)
        let r2 = (-b - Math.sqrt(d)/2*a)
        console.log(`Duas raízes reais de valor ${r1} e ${r2}`)
    }
}
  
  



  