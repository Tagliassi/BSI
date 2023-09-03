// Classe Arma
export class Arma {
  constructor(nome, dano) {
      this.nome = nome;
      this.dano = dano;
  }

  aumentarDano(personagem) {
      personagem.dano += this.dano;
  }

  adicionarArmaInventario(){
    adicionarItemInventario(this.nome)
  }

  verificarSeTemArma(){
    if (this.player.posicaoAtual[0] === 3 && this.player.posicaoAtual[1] === 0) {
      console.log("O personagem encontrou uma arma, foi adicionada ao seu inventario.");
      adicionarArmaInventario()
    }
  }

}
