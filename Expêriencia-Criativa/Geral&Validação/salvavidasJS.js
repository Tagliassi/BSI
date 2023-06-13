//para visualizar as execuções do seu código javascript você deve abrir o console no próprio navegador
//você pode fazer isso pressionando a tecla "F12" do seu teclado na sua página web
//ou clicando com o botão direito em qualquer local da tela e escolhe a opção "Inspecionar"
//lembre sempre de selecionar a aba console (figura: console.png)

//Para um arquivo ser reconhecido como um arquivo JavaScript, ele deve ser salvo com a extensão ".js"
//Exemplo: script.js, arquivo.js, nome-do-arquivo.js, outro_exemplo.js
//preferencialmente sempre com letras minúsculas, e NUNCA usar caracteres especiais como acentos ou símbolos


//Imprimir uma mensagem no CONSOLE
//Essa mensagem será vista no console do navegador, e NÃO na página HTML
//Pode ser utilizado aspas simples ('') ou aspas duplas ("") para escrever um texto (tipo: string)
console.log('Mensagem no CONSOLE com aspas simples!');
console.log("Mensagem no CONSOLE com aspas duplas!");

//Tipos para números
//33 - número inteiro
//33.5 - número real
//NaN - Not a Number (não é um número)
//Com os números podemos realizar operações aritméticas, imprimir valores direto no console ou mostrar ao usuário
//Quando imprimimos um número não precisamos utilizar as aspas
console.log(33); // imprime o 33
console.log(33.5); // imprime o 33.5
console.log(33 + 33.5); // imprime o resultado da soma (66.5)
console.log(33 / "blabla"); // imprime o resultado da divisão de 33 pela string "blabla" (NaN - Não é um número)
console.log("A idade da profe Marina é: " + 31); // imprime a concatenação da string dentro das aspas com o número (A idade da profe Marina é: 33)

//Tipo de dado booleano
//só pode ser VERDADEIRO ou FALSO
//Geralmente utilizamos para checar um determinado resultado
//Por exemplo, se estivermos fazendo um site que precise verificar se a idade do usuário é maior que 18 anos
//podemos fazer uma função, que recebe a idade digitada pelo usuário e retorna verdadeiro caso seja maior que 18 e falso caso seja menor que 18
function verificaMaioridade(idade) {
    if(idade >= 18) {
        console.log(true);
    }
    else {
        console.log(false);
    }
}

//Pop-ups de alerta
//Existem três tipos de popup de alerta no JavaScript
//alert - abre uma pop-up com uma mensagem em forma de alerta ao usuário
//confirm - abre uma pop-up com uma mensagem de confirmação ao usuário
//prompt - abre uma pop-up onde o usuário pode inserir uma informação

function alerta() {
    alert('Isso é uma mensagem de alerta!');
}

function confirma() {
    //salvo o input do usuário na variável resposta
    resposta = confirm("Isso é uma mensagem de confirmação!");

    //se a resposta do usuário for a opção OK (opção 1)
    if(resposta == 1) {
        //mensagem de feedback no console
        console.log("Clicou OK")
        //retorno verdadeiro
        return true;
    }
    //se não for
    else {
        //mensagem de feedback no console
        console.log("Clicou Cancelar")
        //retorno falso
        return false;
    }
}

function entrada() {
    //salvo o que o usuário digitar em uma variável
    nome = prompt("Isso é uma mensagem com entrada do usuário!");
    //imprimimos o que foi digitado no console (para feedback)
    console.log(nome)
    //retorno o que o usuário digitou
    return nome;
}

//Exemplo de validação se o campo contém texto
function validaInputVazio() {
    //Primeiro vamos pegar o texto que o usuário digitou dentro do input no html e salvar em uma variável
    //Para isso vamos utilizar o objeto document do JavaScript
    //Esse objeto busca elementos dentro do nosso documento html
    //Esse objeto possui uma função chamada getElementById(id)
    //Essa função recebe como parâmetro um determinado id
    //e realiza a busca de um elemento que possua o mesmo id que foi informado
    //ao final da chamada da função, colocamos um ".value" pois queremos o VALOR fornecido pelo usuário

    texto = document.getElementById("name").value;

    //Vamos ver se dentro dessa variável está o mesmo texto que o usuario digitou?
    //Vou imprimir no console essa variável para verificar
    console.log(texto);
    
    //Agora vamos fazer uma validação deste texto
    //Caso o usuário não tenha digitado texto nenhum, vou exibir um alerta pedindo para que ele digite um texto válido
    //Caso contrário vou mostrar esse elemento na PÁGINA WEB
    
    //Vamos começar checando se o texto é vazio ou não
    if(texto == "") {
        //Se não tiver digitado nada, mostra o alerta
        alert('Digite um texto válido');
    }
    else {
        //vamos pegar o conteúdo já existente no nosso HTML atual, para adicionar a palavra digitada ao nosso site
        var conteudoExistente = document.body.innerHTML;
        //agora vamos atribuir ao conteúdo já existente o próprio conteúdo em si, adicionamos uma quebra de linha
        //em seguida do texto que foi digitado pelo usuário
        document.body.innerHTML = conteudoExistente + "<br>" + texto;
    }
}

//Exemplo de validação quantidade de caracteres de um texto

function validaQuantidadeDeCaracteres() {
    //Primeiro vamos pegar o texto que o usuário digitou dentro do input no html e salvar em uma variável
    telefone = document.getElementById("tel").value;

    //Vamos ver se dentro dessa variável está o mesmo texto que o usuario digitou?
    //Vou imprimir no console essa variável para verificar
    console.log(telefone);

    //vamos verificar se o telefone possui menos de 8 caracteres
    //para isso usamos o ".length" que signitica tamanho em inglês
    //não queremos saber se o valor do telefone é menor que 8
    //e sim se a quantidade de caracteres, ou seja, o tamanho do texto, é menor que 8
    if(telefone.length < 9) {
        //Se for menor que 9, mostra o alerta
        alert("Telefone inválido, digite um telefone válido!")
    }
    else {
        //se não, imprime o telefone digitado na PÁGINA WEB (da mesma forma que fizemos na função validaInputVazio())
        var conteudoExistente = document.body.innerHTML;
        document.body.innerHTML = conteudoExistente + "<br>" + telefone;
    }
}