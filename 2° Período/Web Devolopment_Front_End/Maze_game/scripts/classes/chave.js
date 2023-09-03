// Classe Chave
export class Chave {
    constructor(tipoDeChave) {
        this.tipoDeChave = tipoDeChave;
    }

    adicionarChaveInventario(){
        adicionarItemInventario(this.tipoDeChave)
    }

    verificarSeTemChave(){
        if (this.player.posicaoAtual[0] === 0 && this.player.posicaoAtual[1] === 6 || this.player.posicaoAtual[0] === 4 && this.player.posicaoAtual[1] === 2) {
          console.log("O personagem encontrou uma chave, foi adicionada ao seu inventario.");
          adicionarChaveInventario()
        }
      }
  }