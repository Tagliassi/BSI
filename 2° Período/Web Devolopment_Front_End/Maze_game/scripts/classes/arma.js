import { Item } from './item.js';
// Classe Arma
export class Arma extends Item {
  constructor(nome, dano) {
    super(nome);
    this.dano = dano;
  }

  verificarSeTemArmaEColetar(personagem) {
    const localizacaoAtual = this.obterLocalizacaoExata();

    if (localizacaoAtual.x === 3 && localizacaoAtual.y === 0) {
      if (!personagem.arma) {
        console.log(`O personagem encontrou uma arma (${this.nome}) e a adicionou ao seu inventário.`);
        this.coletar(personagem); // Chame o método de coleta da classe base
      } else {
        console.log(`O personagem já possui uma arma, não foi possível coletar a arma (${this.nome}).`);
      }
    }
  }
}
