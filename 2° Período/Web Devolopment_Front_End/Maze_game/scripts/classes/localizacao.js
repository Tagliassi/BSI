import { Chave } from "./chave.js";
import { Monstro } from "./../mobs/monstro.js";
import { Evento } from "./evento.js";
import { Arma } from "./arma.js";
import { Armadilha } from "./armadilha.js";
import { Porta } from "./porta.js";
import { Portal } from "./portal.js";
import { Cura } from "./cura.js";
import { Saida } from "./saida.js";

// Classe Localizacao
export class Localizacao {
  constructor(ativado = true, name, descricao, imagem, obj) {
    this.nome = name;
    this.descricao = descricao;
    this.monstro = null;
    this.evento = null;
    this.item = null;
    this.personagem = false;
    this.imagem = imagem;
    this.obj = obj;
    this.ativado = ativado;
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

  adicionarPersonagem() {
    this.personagem = true;
  }

  removerPersonagem() {
    this.personagem = false;
  }
  
  monsterExist() {
    return (this.obj instanceof Monstro);
  }
  
  mensagemAdicional() {
    if(this.obj instanceof Monstro){
      this.descricao += "Você está enfrentando um monstro.";
      this.descricao += `\n\n${this.obj.apresentar()}`
      this.descricao += "\n\nImediatamente ele avança sobre você, gritando:.";
      this.descricao += `\n\n${this.obj.gritar()}`
      this.descricao += "\n\nVocê saca sua arma e fica em posição, agora resta esperar o momento certo para realizar seu ataque.";
    }
    
    if(this.obj instanceof Chave){
      this.descricao = this.descricao + "Você encontrou um objeto: Chave Verde.";
    }
    
    if(this.obj instanceof Armadilha){
      this.descricao += "Cuidado! Você caiu em uma armadilha.";
    }
    
    if(this.obj instanceof Cura){
      this.descricao += "encontrou uma poção de cura.";
      this.descricao += "\n\nVocê olha para o chão e ecnontra um poção coberta de musgo, no desespero você a toma\n\n- Sinto-me mais aliviado";
    }
    
    if(this.obj instanceof Arma){
      this.descricao += "Você encontrou uma nova arma, e diz.\n\n- Agora posso finalmente batalhar.";
    }
    
    if(this.obj instanceof Porta){
      this.descricao += "Você encontrou uma porta.";
      this.descricao += "\n\nParece está trancada, você não consegue ver o que tem do outro lado, mas consegue ouvir alguns musmurros.\n\n- muhr.. murr...";
    }
    
    if(this.obj instanceof Portal){
      this.descricao += "Você entrou em um portal misterioso. Parece não funcionar mas te deixa intrigado.";
    }
    
    if(this.obj instanceof Saida){
      this.descricao += "- Enfim a jornada terminou.";
    }

    this.descricao += "\n\n";
  }
}
