export class Item {
    constructor(nome) {
      this.nome = nome;
    }
  
    coletar(personagem) {
      personagem.adicionarItemInventario(this);
    }
  }
  