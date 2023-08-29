class Monstro {
    constructor(nome, vida, dano, defesa, critico) {
      this.nome = nome;
      this.vida = vida;
      this.dano = dano;
      this.defesa = defesa; // 0.0 a 1.0
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
  
class Personagem {
    constructor(nome) {
        this.nome = nome;
        this.vida = 100;
        this.dano = 10;
        this.defesa = 0; 
        this.inventario = [];
}

apresentar() {
    console.log(`Olá, meu nome é ${this.nome}`);
}

atacar(monstro) {
    let danoTotal = this.dano * (1 - monstro.defesa);
    monstro.vida -= danoTotal;
}

realizarAtaqueCritico() {
    let valorCritico = Math.random() < 0.7 ? this.dano * 2 : this.dano;
    return valorCritico;
    }
}

class Armadilha {
    constructor(nome, dano) {
        this.nome = nome;
        this.dano = dano;
    }

    gerarDano(personagem) {
        personagem.vida -= this.dano;
    }
}

class Cura {
    constructor(nome, cura) {
        this.nome = nome;
        this.cura = cura;
    }

    aplicarCura(personagem) {
        personagem.vida += this.cura;
    }
}

class Arma {
    constructor(nome, dano) {
        this.nome = nome;
        this.dano = dano;
    }

    aumentarDano(personagem) {
        personagem.dano += this.dano;
    }
}

class Porta {
    constructor(nome, tipoDeChave) {
        this.nome = nome;
        this.tipoDeChave = tipoDeChave;
        this.trancada = true; // Adicionada propriedade para controlar se a porta está trancada
    }

    abrirPorta(chave) {
        if (chave.tipoDeChave === this.tipoDeChave) {
            this.trancada = false;
            console.log(`A porta ${this.nome} foi destrancada.`);
        } else {
            console.log(`A chave não corresponde ao tipo necessário para abrir a porta ${this.nome}.`);
        }
    }
}

class Portal {
    constructor(nome) {
        this.nome = nome;
    }

    teleportarPersonagemAleatoriamente() {
        // Implementar a lógica de teleportação aqui
    }
}

class Chave {
    constructor(tipoDeChave) {
        this.tipoDeChave = tipoDeChave;
    }
}
  