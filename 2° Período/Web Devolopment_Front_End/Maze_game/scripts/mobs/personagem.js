import { Saida } from '../classes/saida.js';
import { updateGameInterface } from './../alterGameInterface.js';

export class Personagem {
  constructor(nome, mapa) {
    this.nome = nome;
    this.vida = 3;
    this.dano = 10;
    this.inventario = [];
    this.mapa = mapa;
    this.mapa.map[4][5].adicionarPersonagem(); // Define a localização inicial onde o jogador inicia

    const botaoBatalha = document.getElementById("fight");
    botaoBatalha.addEventListener("click", () => this.batalhar())
  }

  atualizarCoracoes() {
    const heartsContainer = document.querySelector(".player-status .hearts");
    const caminhoImagemCoracao = "./../../assets/elementos/hearts.png";

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

  atacar(monstro) {
    monstro.apanhar();
  }

  batalhar() {
    this.atacar(this.monstroAtual);
  }
  
  //   iniciarAcao() {
  //     if (this.arma) {
  //       const danoTotal = this.dano + this.arma.dano;
  //       console.log(`${this.nome} atacou com ${this.arma.nome} causando ${danoTotal} de dano.`);
  //     } else {
  //       console.log(`${this.nome} atacou causando ${this.dano} de dano.`);
  //     }

  //     // Verifique se há um monstro na localização atual e inicie uma batalha
  //     const localizacaoAtual = this.obterLocalizacaoExata();
  //     if (localizacaoAtual.monstro) {
  //       this.iniciarBatalhaComMonstro(localizacaoAtual.monstro);
  //     }

  iniciarBatalhaComMonstro(monstro) {
    const batalha = new Batalha(this, monstro);
    batalha.batalhar();
  }

  // Método para adicionar um item ao inventário do jogador, se houver no local onde ele está.
  verificarSeTemItem() {
    const localizacaoAtual = this.obterLocalizacaoExata();
    const item = localizacaoAtual.item;
  }

  adicionarItemInventario(item) {
    this.inventario.push(item);
    if (item) {
      item.coletar(this);
      localizacaoAtual.item = null; // Remova o item do mapa após a coleta
      console.log(`Você coletou ${item.nome}.`);
    }
  }

  adicionarItemInventario(item) {
    this.inventario.push(item);
  }

  morrer(nomeMonstro) {
    const heartsContainer = document.querySelector(".player-status .hearts");

    heartsContainer.remove()

    setTimeout(() => {
      alert(`O ${nomeMonstro} o devorou.`);
      location.reload();
    }, 1700);
  }

  //#region Movimentação
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

      // Verifica se é a saida
      if (novaLocalizacao.obj instanceof Saida) {
        alert("Fim de jogo. Parabéns!");
        location.reload();
      }

      // Atualize a posição do personagem
      localizacaoAtual.personagem = false;
      novaLocalizacao.personagem = true;

      // Algoritimo para verificar salas ao redor
      const cima = x > 0 ? this.mapa.map[x - 1][y] : null;
      const baixo = x < this.mapa.map.length - 1 ? this.mapa.map[x + 1][y] : null;
      const esquerda = y > 0 ? this.mapa.map[x][y - 1] : null;
      const direita = y < this.mapa.map[x].length - 1 ? this.mapa.map[x][y + 1] : null;

      document.getElementById("move-up").disabled = false;
      document.getElementById("move-down").disabled = false;
      document.getElementById("move-left").disabled = false;
      document.getElementById("move-right").disabled = false;

      if (!cima.ativado) {
        document.getElementById("move-up").disabled = true;
      }
      if (!baixo.ativado) {
        document.getElementById("move-down").disabled = true;
      }
      if (!esquerda.ativado) {
        document.getElementById("move-left").disabled = true;
      }
      if (!direita.ativado) {
        document.getElementById("move-right").disabled = true;
      }

      // Verifica se é a sala do monstro ou não
      const monsterLifeContainer = document.getElementsByClassName("monster-status")[0];
      const botaoBatalha = document.getElementById("fight");

      console.log(novaLocalizacao);
      if (novaLocalizacao.monsterExist()) {
        novaLocalizacao.obj.atualizarCoracoes();

        monsterLifeContainer.style.display = "block";
        botaoBatalha.style.display = "block";

        novaLocalizacao.obj.lutar(this);
        this.monstroAtual = novaLocalizacao.obj;
      } else {
        monsterLifeContainer.style.display = "none";
        botaoBatalha.style.display = "none";
      }

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
    return null;
  }

  //#endregion
}
