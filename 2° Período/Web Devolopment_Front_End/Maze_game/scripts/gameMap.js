import { Localizacao } from "./classes/localizacao.js";
import { Chave } from "./classes/chave.js";
import { Monstro } from "./mobs/monstro.js";
import { Evento } from "./classes/evento.js";
import { Arma } from "./classes/arma.js";
import { Armadilha } from "./classes/armadilha.js";
import { Porta } from "./classes/porta.js";
import { Portal } from "./classes/portal.js";
import { Cura } from "./classes/cura.js";

// Classe GameMap
export class GameMap {
  constructor() {
    // Definir mapa bidimensional
    this.map = [
      [
        new Localizacao("void", "Você está na localização [0][0].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [0][1].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [0][2].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [0][3].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [0][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [0][5].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("chave", "Você está na localização [0][6].", "./../../assets/cenario/tela-inicial.png", this.item = new Chave("Chave Verde")),
        new Localizacao("void", "Você está na localização [0][7].", "./../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Você está na localização [1][0].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [1][1].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [1][2].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("parede", "Você está na localização [1][3].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [1][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("monstro", "Você está na localização [1][5].", "./../../assets/monstros/creeper-boss.png", this.monstro = new Monstro("Creeper", 3, 1)),
        new Localizacao("void", "Você está na localização [1][6].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [1][7].", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Você está na localização [2][0].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [2][1].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [2][2].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("armadilha", "Você está na localização [2][3].", "./../../assets/cenario/tela-inicial.png", this.evento = new Armadilha("Piscina de Veneno", 1)),
        new Localizacao("parede", "Você está na localização [2][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("narrativa", "Você está na localização [2][5].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("cura", "Você está na localização [2][6].", "./../../assets/cenario/tela-inicial.png", this.item = new Cura("Super Cura", 3)),
        new Localizacao("void", "Você está na localização [2][7].", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("arma", "Você está na localização [3][0].", "./../../assets/cenario/tela-inicial.png", this.item = new Arma("Espadona", 1)),
        new Localizacao("monstro", "Você está na localização [3][1].", "./../../assets/monstros/maicris-boss.png", this.monstro = new Monstro("Maicris", 3, 1)),
        new Localizacao("porta", "Você está na localização [3][2].", "./../../assets/cenario/tela-inicial.png", this.evento = new Porta("Porta Vermelha", "Chave Vermelha")),
        new Localizacao("personagem", "Você está na localização [3][3].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("nada", "Você está na localização [3][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("arma", "Você está na localização [3][5].", "./../../assets/cenario/tela-inicial.png", this.item = new Arma("Espada", 1)),
        new Localizacao("monstro", "Você está na localização [3][6].", "./../../assets/monstros/capivara.png", this.monstro = new Monstro("Capivara Locona", 3, 1)),
        new Localizacao("void", "Você está na localização [3][7].", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Você está na localização [4][0].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [4][1].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("chave", "Você está na localização [4][2].", "./../../assets/cenario/tela-inicial.png", this.item = new Chave("Chave Vermelha")),
        new Localizacao("nada", "Você está na localização [4][3].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [4][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("armadilha", "Você está na localização [4][5].", "./../../assets/cenario/tela-inicial.png", this.evento = new Armadilha("Piscina de Veneno", 1)),
        new Localizacao("void", "Você está na localização [4][6].", "./../../assets/cenario/simbolo.png"),
        new Localizacao("void", "Você está na localização [4][7].", "./../../assets/cenario/simbolo.png"),
      ],
      [
        new Localizacao("void", "Você está na localização [5][0].", "./../../assets/cenario/simbolo.png"),
        new Localizacao("void", "Você está na localização [5][1].", "./../../assets/cenario/simbolo.png"),
        new Localizacao("void", "Você está na localização [5][2].", "./../../assets/cenario/simbolo.png"),
        new Localizacao("monstro", "Você está na localização [5][3].", "./../../assets/monstros/moscona.png", this.monstro = new Monstro("Moscona", 3, 1)),
        new Localizacao("void", "Você está na localização [5][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("porta", "Você está na localização [5][5].", "./../../assets/cenario/tela-inicial.png", this.evento = new Porta("Porta Verde", "Chave Verde")),
        new Localizacao("void", "Você está na localização [5][6].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [5][7].", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Você está na localização [6][0].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [6][1].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [6][2].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("portal", "Você está na localização [6][3].", "./../../assets/cenario/tela-inicial.png", this.evento = new Portal("Portal")),
        new Localizacao("void", "Você está na localização [6][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("saida", "Você está na localização [6][5].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [6][6].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [6][7].", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Você está na localização [7][0].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][1].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][2].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][3].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][4].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][5].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][6].", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está na localização [7][7].", "./../../assets/cenario/tela-inicial.png"),
      ],
    ];
  }
}