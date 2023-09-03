// Função para atualizar a interface do jogo
export function updateGameInterface(caminhoImg, novoTexto) {
  alterarFundo(caminhoImg);
  alterarTexto(novoTexto);
}

export function alterarFundo(caminhoImg){
  const fundo = document.querySelector('img');

  fundo.src = caminhoImg; 
}

export function alterarTexto(novoTexto){
  const texto = document.querySelector('.game-text');

  texto.innerText = novoTexto;
}