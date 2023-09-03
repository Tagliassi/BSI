// Classe Armadilha
class Armadilha {
  constructor(nome, dano) {
      this.nome = nome;
      this.dano = dano;
  }

  gerarDano(personagem) {
      personagem.vida -= this.dano;
  }
}

