import {updateGameInterface} from './../alterGameInterface.js';

export class Personagem {
  constructor(nome, mapa) {
    this.nome = nome;
    this.vida = 3;
    this.dano = 10;
    this.inventario = [];
    this.mapa = mapa;
    this.mapa.map[4][5].adicionarPersonagem(); // Define a localização inicial
  }

  // Método para atualizar os corações com base na vida atual do jogador
  atualizarCoracoes() {
    const heartsContainer = document.querySelector(".hearts");
    const caminhoImagemCoracao = "./../../assets/hearts.png";

    // Remova todos os corações existentes
    heartsContainer.innerHTML = "";

    // Crie corações com base na vida atual
    for (let i = 0; i < this.vida; i++) {
      const heart = document.createElement("img");
      heart.src = caminhoImagemCoracao;

      heart.classList.add("heart");
      heartsContainer.appendChild(heart);
    }
  }

  apresentar() {
    return `Olá, meu nome é ${this.nome}`;
  }

  atacar() {
    iniciarBatalha();
  }

  // Método para adicionar um item ao inventário do jogador
  adicionarItemInventario(item) {
    this.inventario.push(item);
  }

  movePersonagem(x, y) {
    if (
      x >= 0 &&
      x < this.mapa.map.length &&
      y >= 0 &&
      y < this.mapa.map[x].length
    ) {
      // Remova o personagem da localização atual
      const localizacaoAtual = this.obterLocalizacaoExata();
      localizacaoAtual.removerPersonagem();

      // Adicione o personagem à nova localização
      const novaLocalizacao = this.mapa.map[x][y];
      novaLocalizacao.adicionarPersonagem();

      // Atualize a posição do personagem
      localizacaoAtual.personagem = false;
      novaLocalizacao.personagem = true;
      console.log(this.obterLocalizacaoExata());

      updateGameInterface(novaLocalizacao.imagem, novaLocalizacao.descricao);
    } else {
      // matar personagem ou lidar com o movimento inválido
    }
  }

  // Função para mover o personagem para a esquerda
  moveBaixo() {
    const localizacao = this.encontrarIndiceDoObjeto(
      this.obterLocalizacaoExata(),
      this.mapa.map
    );

    let x = localizacao.linha + 1;
    let y = localizacao.coluna;

    this.movePersonagem(x, y);
  }

  // Função para mover o personagem para a esquerda
  moveCima() {
    const localizacao = this.encontrarIndiceDoObjeto(
      this.obterLocalizacaoExata(),
      this.mapa.map
    );

    let x = localizacao.linha - 1;
    let y = localizacao.coluna;

    this.movePersonagem(x, y);
  }

  // Função para mover o personagem para a esquerda
  moveEsquerda() {
    const localizacao = this.encontrarIndiceDoObjeto(
      this.obterLocalizacaoExata(),
      this.mapa.map
    );

    let x = localizacao.linha;
    let y = localizacao.coluna - 1; // Mova para a esquerda

    this.movePersonagem(x, y);
  }

  // Função para mover o personagem para a direita
  moveDireita() {
    const localizacao = this.encontrarIndiceDoObjeto(
      this.obterLocalizacaoExata(),
      this.mapa.map
    );

    let x = localizacao.linha;
    let y = localizacao.coluna + 1; // Mova para a direita

    this.movePersonagem(x, y);
  }

  // Obtém a localização exata do personagem
  obterLocalizacaoExata() {
    const matriz = this.mapa.map;
    for (let i = 0; i < matriz.length; i++) {
      for (let k = 0; k < matriz[i].length; k++) {
        if (matriz[i][k].personagem) {
          return matriz[i][k];
        }
      }
    }
  }

  // Encontra index do objeto
  encontrarIndiceDoObjeto(objetoProcurado, matriz) {
    for (let i = 0; i < matriz.length; i++) {
      for (let j = 0; j < matriz[i].length; j++) {
        if (JSON.stringify(matriz[i][j]) === JSON.stringify(objetoProcurado)) {
          return { linha: i, coluna: j };
        }
      }
    }
    return null; // Se o objeto não for encontrado, retorna null
  }
}
