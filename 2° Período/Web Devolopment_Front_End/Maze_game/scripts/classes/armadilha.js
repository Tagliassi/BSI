// Classe Armadilha
export class Armadilha {
  constructor(nome, dano) {
    this.nome = nome;
    this.dano = dano;
  }

  gerarDano(personagem) {
    personagem.vida -= this.dano;
    console.log(`O personagem foi atingido pela armadilha "${this.nome}" e perdeu ${this.dano} pontos de vida.`);
  }

  verificarSeTemArmadilha(personagem) {
    const localizacaoAtual = personagem.obterLocalizacaoExata();

    if (
      (localizacaoAtual.x === 2 && localizacaoAtual.y === 3) ||
      (localizacaoAtual.x === 4 && localizacaoAtual.y === 5)
    ) {
      console.log("O personagem encontrou uma armadilha e tomou dano.");
      this.gerarDano(personagem);
    }
  }
}
