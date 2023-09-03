// Classe Cura
class Cura {
  constructor(nome, cura) {
      this.nome = nome;
      this.cura = cura;
  }

  aplicarCura(personagem) {
      personagem.vida += this.cura;
  }
}
