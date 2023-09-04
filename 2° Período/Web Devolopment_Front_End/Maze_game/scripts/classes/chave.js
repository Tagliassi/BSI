// Classe Chave
export class Chave extends Item {
    constructor(tipoDeChave) {
      super(`Chave ${tipoDeChave}`);
      this.tipoDeChave = tipoDeChave;
    }

    verificarSeTemChave() {
        const localizacaoAtual = this.obterLocalizacaoExata();
    
        if (
          (localizacaoAtual.x === 0 && localizacaoAtual.y === 6) ||
          (localizacaoAtual.x === 4 && localizacaoAtual.y === 2)
        ) {
          console.log(`O personagem encontrou uma chave (${this.tipoDeChave}), foi adicionada ao seu inventário.`);
          this.coletar(this); // Chame o método de coleta da classe base
        }
    }
}