export function alterarFundo(caminhoImg){
  const fundo = document.querySelector('img');

  imgElement.src = caminhoImg; 
}

export function alterarTexto(novoTexto){
  const texto = document.querySelector('.game-description');

  texto.innerText = novoTexto;
}