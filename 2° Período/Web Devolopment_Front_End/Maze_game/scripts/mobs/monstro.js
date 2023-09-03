// Classe Monstro
export class Monstro {
    constructor(nome, vida, dano) {
        this.nome = nome;
        this.vida = vida;
        this.dano = dano;
    }
  
    apresentar() {
        console.log(`Olá, meu nome é ${this.nome} e sou um MONSTRO HORRÍVELll !!! MUAHUAHAUAHAHA`);
    }
  
    atacar(personagem) {
        personagem.vida -= this.dano;
    }
  
  }