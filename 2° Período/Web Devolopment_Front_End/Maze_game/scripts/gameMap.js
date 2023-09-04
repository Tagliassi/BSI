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
        new Localizacao("void", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Você deu de cara com uma parede, parece que vai ter que voltar e tentar outro caminho.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você continua a andar e não encontra nada aqui. Pela sua sorte não encontrou ninguém, mais o frio e a tensão no ar se aumenta.", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Você continua a andar..", "./../../assets/cenario/caminho2.png"),
        new Localizacao("void", "Você deu de cara com uma parede, parece que vai ter que voltar e tentar outro caminho.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você continua a andar e não encontra nada aqui. Pela sua sorte não encontrou ninguém, mais o frio e a tensão no ar se aumenta.", "./../../assets/cenario/caminho2.png"),
        new Localizacao("chave", "Você está com frio e não encontrou nada.", "./../../assets/cenario/tela-inicial.png", this.item = new Chave("Chave Verde")),
        new Localizacao("void", "Aqui não tem nada.", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Você está com frio e não encontrou nada.", "./../../assets/cenario/caminho2.png"),
        new Localizacao("parede", "Você está com frio e não encontrou nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/caminho1.png"),
        new Localizacao("monstro", "", "./../../assets/monstros/creeper-boss.png", this.monstro = new Monstro("Creeper", 3, 1)),
        new Localizacao("void", "Você deu de cara com uma parede, parece que vai ter que voltar e tentar outro caminho..", "./../../assets/cenario/caminho2.png"),
        new Localizacao("void", "Você deu de cara com uma parede, parece que vai ter que voltar e tentar outro caminho.", "./../../assets/cenario/caminho1.png"),
      ],
      [
        new Localizacao("void", "Aqui não tem nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Aqui não tem nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você continua a andar..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("armadilha", "Você encontrou uma armadilha, uma piscina de veneno terrível e toma dano", "./../../assets/cenario/tela-inicial.png", this.evento = new Armadilha("Piscina de Veneno", 1)),
        new Localizacao("parede", "Você deu de cara com uma parede, parece que vai ter que voltar e tentar outro caminho..", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("narrativa", "Você encontrou o homem morto", "./../../assets/cenario/caminho2.png"),
        new Localizacao("cura", "Você encontrou algo que vai te alegrar", "./../../assets/cenario/tela-inicial.png", this.item = new Cura("Super Cura", 3)),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("arma", "Você olha ao redor e vê que encontrou uma arma.", "./../../assets/cenario/tela-inicial.png", this.item = new Arma("Espadona", 1)),
        new Localizacao("monstro", "Você encontrou um monstro terrível.", "./../../assets/monstros/maicris-boss.png", this.monstro = new Monstro("Maicris", 3, 1)),
        new Localizacao("porta", "Você encontrou uma porta, parece que precisa de uma chave para abri-la.", "./../../assets/cenario/tela-inicial.png", this.evento = new Porta("Porta Vermelha", "Chave Vermelha")),
        new Localizacao("personagem", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("nada", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/caminho1.png"),
        new Localizacao("arma", "Você olha ao redor e vê que encontrou uma arma.", "./../../assets/cenario/tela-inicial.png", this.item = new Arma("Espada", 1)),
        new Localizacao("monstro", "Você encontrou um monstro terrível.", "./../../assets/monstros/capivara.png", this.monstro = new Monstro("Capivara Locona", 3, 1)),
        new Localizacao("void", "Aqui não tem nada.", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Você está seguindo um corredor, ao fundo parece haver algo.. Você segue e olha ao redor.", "./../../assets/cenario/caminho2.png"),
        new Localizacao("void", "Você segue caminhando no corredor.", "./../../assets/cenario/caminho2.png"),
        new Localizacao("chave", "Você encontrou uma chave, talvez ela abra uma porta", "./../../assets/cenario/tela-inicial.png", this.item = new Chave("Chave Vermelha")),
        new Localizacao("nada", "Você está com frio e não encontrou nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você continua a andar..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("armadilha", "Você encontrou uma armadilha, uma piscina de veneno terrível e toma dano", "./../../assets/cenario/tela-inicial.png", this.evento = new Armadilha("Piscina de Veneno", 1)),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho2.png"),
        new Localizacao("void", "Você está seguindo um corredor, ao fundo parece haver algo.. Você segue e olha ao redor..", "./../../assets/cenario/caminho1.png"),
      ],
      [
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Você está seguindo um corredor, ao fundo parece haver algo.. Você segue e olha ao redor.", "./../../assets/cenario/caminho2.png"),
        new Localizacao("monstro", "Você encontrou um monstro terrível.", "./../../assets/monstros/moscona.png", this.monstro = new Monstro("Moscona", 3, 1)),
        new Localizacao("void", "Você segue caminhando no corredor.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("porta", "Você deu de cara com uma porta, parece está trancada e acorrentada. Você parece saber institivamente onde está a chave..", "./../../assets/cenario/porta1.png", this.evento = new Porta("Porta Verde", "Chave Verde")),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho2.png"),
      ],
      [
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("portal", "Você continua a andar...", "./../../assets/cenario/porta2.png", this.evento = new Portal("Portal")),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho2.png"),
        new Localizacao("saida", "Você encontrou a saída, parabéns!", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está com frio e não encontrou nada..", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
      ],
      [
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está com frio e não encontrou nada.", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/caminho1.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Você está com frio e não encontrou nada.", "./../../assets/cenario/caminho2.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho2.png"),
        new Localizacao("void", "Você está num caminho frio e escuro, você olha para o fundo e não encontra nada.", "./../../assets/cenario/tela-inicial.png"),
        new Localizacao("void", "Aqui não tem nada..", "./../../assets/cenario/caminho1.png"),
      ],
    ];
  }
}