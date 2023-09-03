// Classe Arma
class Arma {
  constructor(nome, dano) {
      this.nome = nome;
      this.dano = dano;
  }

  aumentarDano(personagem) {
      personagem.dano += this.dano;
  }
}
