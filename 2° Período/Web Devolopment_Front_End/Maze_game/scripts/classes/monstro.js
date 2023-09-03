// Classe Monstro
class Monstro {
  constructor(nome, vida, dano, defesa, critico) {
      this.nome = nome;
      this.vida = vida;
      this.dano = dano;
      this.defesa = defesa; // Valor entre 0.0 e 1.0
      this.criticoChance = critico;
  }

  apresentar() {
      console.log(`Olá, meu nome é ${this.nome} e sou um MONSTRO HORRÍVELll !!! MUAHUAHAUAHAHA`);
  }

  atacar(personagem) {
      personagem.vida -= this.dano;
  }

  realizarAtaqueCritico() {
      let valorCritico = Math.random() < this.criticoChance ? this.dano * 2 : this.dano;
      return valorCritico;
  }
}