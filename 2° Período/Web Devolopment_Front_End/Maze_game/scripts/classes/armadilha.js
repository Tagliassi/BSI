// Classe Armadilha
export class Armadilha {
  constructor(nome, dano) {
      this.nome = nome;
      this.dano = dano;
  }

  gerarDano(personagem) {
      personagem.vida -= this.dano;
  }

  verificarSeTemArmadilha(){
    if (this.player.posicaoAtual[0] === 2 && this.player.posicaoAtual[1] === 3 || this.player.posicaoAtual[0] === 4 && this.player.posicaoAtual[1] === 5) {
      console.log("O personagem encontrou uma armadilha e tomou dano.");
      this.gerarDano()
    }
  }
}

