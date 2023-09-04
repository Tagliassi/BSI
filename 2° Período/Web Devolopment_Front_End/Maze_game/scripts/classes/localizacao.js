import { Chave } from "./chave.js";
import { Monstro } from "./../mobs/monstro.js";
import { Evento } from "./evento.js";
import { Arma } from "./arma.js";
import { Armadilha } from "./armadilha.js";
import { Porta } from "./porta.js";
import { Portal } from "./portal.js";
import { Cura } from "./cura.js";
// Classe Localizacao
export class Localizacao {
  constructor(name, descricao, imagem, obj) {
      this.nome = name;
      this.descricao = descricao;
      this.monstro = null;
      this.evento = null;
      this.item = null;
      this.personagem = false;
      this.imagem = imagem;
      this.obj = obj;
      this.mensagemAdicional()
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

  mensagemAdicional() {
    console.log(this.obj);
    switch (true) {
      case this.obj instanceof Chave:
        this.descricao += "Você encontrou um objeto: Chave Verde.";
        break;
      case this.obj instanceof Monstro:
        this.descricao += "Você está enfrentando um monstro.";
        break;
      case this.obj instanceof Armadilha:
        this.descricao += "Cuidado! Você caiu em uma armadilha.";
        break;
      case this.obj instanceof Cura:
        this.descricao += "Você encontrou uma poção de cura.";
        break;
      case this.obj instanceof Arma:
        this.descricao += "Você encontrou uma nova arma.";
        break;
      case this.obj instanceof Porta:
        this.descricao += "Você encontrou uma porta.";
        break;
      case this.obj instanceof Portal:
        this.descricao += "Você entrou em um portal misterioso.";
        break;
      default:
        this.descricao += "Você está em uma área desconhecida.\n\n- Estou cansado e com fome.";
    }
    this.descricao += "\n\n";
}
}