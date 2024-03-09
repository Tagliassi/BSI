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

//Sort ordena a própria lista.
let numeros = [1,2,3,4,10,9,8,7,6,5]

console.log(numeros.sort((a,b) =>{
    return a-b;
}))
*/

// Exercise 01

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

const cantores = [
    {nome: "Vinícius de Moraes", estilo: "MPB"},
    {nome: "Rita Lee", estilo: "Rock"},
    {nome: "Marisa monte", estilo: "MPB"},
    {nome: "Legião Urbana", estilo: "Rock"},
    {nome: "Titãs", estilo: "Rock"},
    {nome: "Roupa Nova", estilo: "Pop rock"},
    {nome: "Thiago Iorc", estilo: "Nova MPB"},
    {nome: "Skank", estilo: "Pop rock"}
];

/*
marisa = []

albuns.forEach(element => {
    if(element.cantor == 'Marisa monte'){
        marisa.push(element)
    }
});

console.log(marisa)

const monte = albuns.filter(a => a.cantor == "Marisa monte").map(({nome, ano}) => ({nome,ano}));

console.log(monte)

// Exercise 02

// Criar um objeto para armazenar os cantores e seus álbuns associados
const cantoresEAlbuns = {};

// Iterar sobre a lista de cantores
for ({nome: nomeCantor} of cantores) {
    // Filtrar os álbuns associados a este cantor
    const albunsDoCantor = albuns.filter(album => album.cantor === nomeCantor);
    
    // Extrair apenas os nomes dos álbuns
    const nomesDosAlbuns = albunsDoCantor.map(album => album.nome);
    
    // Armazenar os nomes dos álbuns associados a este cantor
    cantoresEAlbuns[nomeCantor] = nomesDosAlbuns;
}

// Criar uma lista com o nome dos cantores e seus álbuns associados
const listaCantoresEAlbuns = [];

// Iterar sobre o objeto cantoresEAlbuns para formatar a lista final
for (let cantor in cantoresEAlbuns) {
    listaCantoresEAlbuns.push(`${cantor} (${cantoresEAlbuns[cantor].join(', ')})`);
}

// Imprimir a lista final
console.log(listaCantoresEAlbuns);

// Exercise 03

const albunsFiltrados = albuns.filter(album => album.ano<2005);

const somaAlbuns = albunsFiltrados.reduce((total, {nota}) => total + nota, 0);
const media_albuns = somaAlbuns / albunsFiltrados.length;
console.log(media_albuns.toFixed(2));

// Exercise 04 

const cantorTotalAlbuns = []
const cantoresList = []

for ({nome: nomeCantor} of cantores){

    const albunsDoCantor = albuns.filter(album => album.cantor == nomeCantor)
    cantorTotalAlbuns.push(`${nomeCantor}: (${albunsDoCantor.length})`)
    cantoresList.push(nomeCantor)
}

console.log(cantorTotalAlbuns)
console.log(cantoresList)

// Exercise 05

// Mapear a lista de cantoresList para substituir os nomes pelos objetos correspondentes
const novaLista = cantoresList.map(nome => {
    return cantores.find(cantor => cantor.nome === nome);
});

console.log(novaLista);

// Exercise 06

const listaSubstituida = albuns
    .map(album => ({...album, cantor: cantores.filter(c => c.nome === album.cantor)[0] || album.cantor }))

console.log(listaSubstituida)

//other way...

const mapCantores = {}

cantores.forEach(c => mapCantores[c.nome] = c)

console.log(mapCantores)

const listaSubstituida2 = albuns
    .map(album => ({...album, cantor: mapCantores[album.cantor] || album.cantor }))

console.log(listaSubstituida2)
*/

// Exercise 07

// Exercise 08

function media(lista, campo) {
    if (campo) { // Verifica se o campo foi fornecido
        const valores = lista.map(item => item[campo]); // Obtém os valores do campo especificado
        const soma = valores.reduce((acumulador, valor) => acumulador + valor, 0); 
        return soma / lista.length; 
    } else {
        const soma = lista.reduce((acumulador, valor) => acumulador + valor, 0); 
        return soma / lista.length; 
    }
}

const alunos = [
    { nome: "aluno1", nota: 4 },
    { nome: "aluno2", nota: 5 },
    { nome: "aluno3", nota: 3 },
];

const avg = media(alunos, "nota");
console.log(avg); 

const avg2 = media([1, 2, 3, 4, 5]); 
console.log(avg2); 