//exercise 01

function mais(value1, value2){
    return value1 + value2;
};

const mais = function(value1, value2){
    return value1 + value2;
};

const mais = (value1, value2) => value1 + value2;

//exercise 02

const menos = (a,b) => b === undefined ? -a : a-b;

//exercise 03

const ehCrescente = (...list) => {

    for (const element of list) {
        let contador = 1;
        if(element > list[contador]){
            return console.log("Não é crescente")
        }
        contador += 1;
        return console.log(`É crescente ${list}`);
    }
};

//exercise 04

const maior = (...nums) => {
    let maior = nums[0];

    for (n of nums){
        n > maior ? (maior = n) : maior;
    }

    return maior;
};

//exercise 05

const join = (separador, ...elements) => {
    
    let string = '';
    
    for (const element of elements) {
        elements.toString();
        string += element
        if(element !== elements[elements.length-1]){
            string += separador
        }
    }

    return string;
};

//exercise 06

const albuns = [
    {nome: "Mais", cantor: "Marisa monte", ano: 1991, nota: 8.5},
    {nome: "A tempestade", cantor: "Legião Urbana", ano: 1996, nota: 9.5},
    {nome: "Domingo", cantor: "Titãs", ano: 1995, nota: 7.5},
    {nome: "Ouro de Minas", cantor: "Roupa Nova", ano: 2001, nota: 8},
    {nome: "Como estão vocês", cantor: "Titãs", ano: 2003, nota: 7},
    {nome: "Troco Likes", cantor: "Thiago Iorc", ano: 2015, nota: 4.5},
    {nome: "Dois", cantor: "Legião Urbana", ano: 1986, nota: 10},
    {nome: "Radiola", cantor: "Skank", ano: 2004, nota: 6.5},
    {nome: "Roupa acústico", cantor: "Roupa Nova", ano: 2004, nota: 9},
    {nome: "Umbilical", cantor: "Thiago Iorc", ano: 2011, nota: 3.5},
    {nome: "Barulhinho bom", cantor: "Marisa monte", ano: 1996, nota: 7.5},
{nome: "Acústico MTV", cantor: "Capital Inicial", ano: 2000, nota: 8.5},
{nome: "Admirável Chip Novo", cantor: "Pitty", ano: 2003, nota: 9},
{nome: "Cê", cantor: "Caetano Veloso", ano: 2006, nota: 8},
{nome: "Da Lama ao Caos", cantor: "Chico Science & Nação Zumbi", ano: 1994, nota: 9.5},
{nome: "Do Cóccix Até o Pescoço", cantor: "Elza Soares", ano: 2002, nota: 9},
{nome: "Equinócio", cantor: "Secos & Molhados", ano: 1973, nota: 8.5},
{nome: "Iê Iê Iê", cantor: "Arnaldo Antunes", ano: 2009, nota: 7.5},
{nome: "Krig-ha, Bandolo!", cantor: "Raul Seixas", ano: 1973, nota: 10},
{nome: "Libra", cantor: "Zeca Baleiro", ano: 2003, nota: 8},
{nome: "MTV ao Vivo", cantor: "Barão Vermelho", ano: 2005, nota: 8.5},
{nome: "N", cantor: "Nando Reis", ano: 2010, nota: 9},
{nome: "O Dia em Que Faremos Contato", cantor: "Lenine", ano: 1997, nota: 9},
{nome: "Paula Toller", cantor: "Paula Toller", ano: 1998, nota: 8},
{nome: "Que País É Este", cantor: "Legião Urbana", ano: 1987, nota: 9.5},
{nome: "Racional", cantor: "Tim Maia", ano: 1975, nota: 10},
{nome: "Sobrevivendo no Inferno", cantor: "Racionais MC's", ano: 1997, nota: 9.5},
{nome: "Tribalistas", cantor: "Tribalistas", ano: 2002, nota: 8.5},
{nome: "Verdade uma Ilusão", cantor: "Marisa Monte", ano: 2013, nota: 7.5},
{nome: "Vô Imbolá", cantor: "Zeca Pagodinho", ano: 1996, nota: 8},
{nome: "Zé Ramalho", cantor: "Zé Ramalho", ano: 1978, nota: 9}
];

function unicos(list, camp){

    let obj = [];

    list.forEach(element => {
        const {[camp]: value} = element
        obj.includes(value) ? null : obj.push(value)
    });

    return obj
}

const cantores = unicos(albuns, 'cantor');

//exercise 07

function fibRecursivo(n) {
    if (n === 0) return 1;
    if (n === 1) return 1;

    return fibRecursivo(n - 1) + fibRecursivo(n - 2);
}

function fibIterativo(n) {
    if (n === 0) return 1;
    if (n === 1) return 1;

    let a = 1;
    let b = 1;

    for (let i = 2; i <= n; i++) {
        const temp = a + b;
        a = b;
        b = temp;
    }

    return b;
}

//exercise 08

function mapear(operatorfunction, nums){

    let newNums = [];

    for (const num of nums) {
        newNums.push(operatorfunction(num))
    }

    return newNums;
}

const dobro = mapear(x => x * 2, [1, 2, 3, 4]);
console.log(dobro);

//exercise 09

function Collatz(elementoInicial) {
    let elementoAtual = elementoInicial;

    return function() {
        if (elementoAtual % 2 === 0) {
            elementoAtual = elementoAtual / 2;
        } else {
            elementoAtual = (elementoAtual * 3) + 1;
        }
        return elementoAtual;
    };
}

const seq = Collatz(5);
console.log(seq()); //16
console.log(seq()); //8
console.log(seq()); //4
console.log(seq()); //2
console.log(seq()); //1

//exercise 10

const verbose = (fn) => {
    return function(...args) {
        const result = fn(...args);
        console.log(`${fn.name}(${args.join(", ")}) = ${result}`);
        return result;
    };
};

const soma = (a, b) => a + b;
const sum = verbose(soma);

let x = sum(5, 2); //Imprime soma(5, 2) = 7
console.log(x); //Imprime 7

//exercise 11

const fixar = (f, ...args) => {
    return function(...addArgs){
        return f(...args, ...addArgs)
    };
};

const somar = (a, b) => a + b;

// Fixar a função somar com o primeiro argumento fixo sendo 5
const somarCom5 = fixar(somar, 5);

console.log(somarCom5(3)); // Retorna 8, pois 5 + 3 = 8
console.log(somarCom5(10)); // Retorna 15, pois 5 + 10 = 15