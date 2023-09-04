// Classe Cura
export class Cura extends Item {
  constructor(nome, cura) {
    super(nome);
    this.cura = cura;
  }

  verificarSeTemCura() {
    const localizacaoAtual = this.obterLocalizacaoExata();

    if (localizacaoAtual.x === 2 && localizacaoAtual.y === 6) {
      console.log(`O personagem encontrou uma super cura (${this.nome}), foi adicionada ao seu inventário.`);
      this.coletar(this); // Chame o método de coleta da classe base
    }
  }

  aplicarCura(personagem) {
    personagem.vida += this.cura;
  }
}
