/*

// forEach recebe uma função que é executada uma vez para cada elemento dentro da lista
[1,2,3,4].forEach(x => console.log("item " + x))

//filter retorna uma cópia da lista, contendo apenas os elementos que atendam a um determinado critério
[1,2,3,4,5,6].filter(x => x % 2 === 0).forEach(x => console.log(x));

//flat irá atuar com uma lista que tenha outras listas dentro. 
//Ele retira os elementos de dentro das listas internas, colocando-os na lista principal.
const elementos = [1, [2,3], [4], [[5]], 6];
console.log(elementos.flat());
//imprime 1,2,3,4,[5],6
console.log(elementos.flat(2));
//imprime 1,2,3,4,5,6

// O map substitui o elemento pelo que for retornado, criando uma nova lista
[1,2,3,4,5,6].map(x => x * 10).forEach(x => console.log(x));

// O flatMap combina um comando map com um comando flat(1) de maneira eficiente
const coordenadas = [
    {x: 12.5, y: 17.2},
    {x: 27.4, y: 13.0},
    {x: 14.7, y: 12.0},
];
console.log(coordenadas.map(c => Object.values(c)));
//[ [ 12.5, 17.2 ], [ 27.4, 13 ], [ 14.7, 12 ] ]
console.log(coordenadas.flatMap(c => Object.values(c)));
//[ 12.5, 17.2, 27.4, 13, 14.7, 12 ]

//A função de redução deve retornar o próximo valor do acumulador. 
//Por exemplo,para somar todos os elementos de uma lista.
const soma = [1, 2, 3, 4].reduce((a, e) => a + e);
console.log("Soma:", soma);

*/

//Sort ordena a própria lista.
let numeros = [1,2,3,4,10,9,8,7,6,5]

console.log(numeros.sort((a,b) =>{
    return a-b;
}))