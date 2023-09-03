// Classe Localizacao
export class Localizacao {
  constructor(name, descricao, imagem) {
      this.nome = name;
      this.descricao = descricao;
      this.monstro = null;
      this.evento = null;
      this.item = null;
      this.personagem = false;
      this.imagem = imagem;
  }

  // Método para definir um monstro no local
  setMonster(monster) {
      this.monster = monster;
  }

  // Método para definir um evento no local
  setEvent(evento) {
      this.evento = evento;
  }

  // Método para definir um item no local
  setItem(item) {
      this.item = item;
  }

  adicionarPersonagem(){
    this.personagem = true;
  }  
  
  removerPersonagem(){
    this.personagem = false;
  }  
}