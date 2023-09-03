// Classe Cura
export class Cura {
  constructor(nome, cura) {
      this.nome = nome;
      this.cura = cura;
  }

  adicionarCuraInventario(){
    adicionarItemInventario(this.nome)
  }

  aplicarCura(personagem) {
      personagem.vida += this.cura;
  }

  verificarSeTemCura(){
    if (this.player.posicaoAtual[0] === 2 && this.player.posicaoAtual[1] === 6) {
      console.log("O personagem encontrou uma super cura, foi adicionada ao seu inventario.");
      adicionarCuraInventario()
    }
  }
  
}
