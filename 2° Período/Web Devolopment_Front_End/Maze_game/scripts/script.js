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

// Classe Personagem
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

    // Método para adicionar um item ao inventário do jogador
    adicionarItemInventario(item) {
        this.inventario.push(item);
    }
}

// Classe Armadilha
class Armadilha {
    constructor(nome, dano) {
        this.nome = nome;
        this.dano = dano;
    }

    gerarDano(personagem) {
        personagem.vida -= this.dano;
    }
}

// Classe Localizacao
class Localizacao {
    constructor(name, descricao) {
        this.nome = name;
        this.descricao = descricao;
        this.monstro = null;
        this.evento = null;
        this.item = null;
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
}

// Classe Evento
class Evento {
    constructor(descricao) {
        this.descricao = descricao;
    }
}

// Classe GameMap
class GameMap {
    constructor() {
        // Definir mapa bidimensional
        this.map = [
            [new Localizacao("Floresta", "Você está na floresta."), new Localizacao("Caverna", "Você está em uma caverna.")],
            [new Localizacao("Montanha", "Você está na montanha."), new Localizacao("Cidade", "Você está na cidade.")],
        ];
        this.LocalizacaoAtual = this.map[0][0]; // Comece na primeira localização
    }

    // Método para mover o jogador para uma localização específica
    movePersonagem(x, y) {
        if (x >= 0 && x < this.map.length && y >= 0 && y < this.map[0].length) {
            this.LocalizacaoAtual = this.map[x][y];
        }
    }
}

// Função para atualizar a interface do jogo
function updateGameInterface() {
    // Implemente a lógica para atualizar a interface do jogo aqui
}

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

// Classe Arma
class Arma {
    constructor(nome, dano) {
        this.nome = nome;
        this.dano = dano;
    }

    aumentarDano(personagem) {
        personagem.dano += this.dano;
    }
}

// Classe Porta
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

// Classe Portal
class Portal {
    constructor(nome) {
        this.nome = nome;
    }

    teleportarPersonagemAleatoriamente() {
        // Implementar a lógica de teleportação aqui
    }
}

// Classe Chave
class Chave {
    constructor(tipoDeChave) {
        this.tipoDeChave = tipoDeChave;
    }
}

// Função para iniciar o jogo
function startGame() {
    const playerName = prompt("Qual é o seu nome?");
    const player = new Personagem(playerName);
    const gameMap = new GameMap();

    // Inicialize a interface do jogo
    updateGameInterface();

    // Implemente o loop do jogo aqui, permitindo que o jogador faça escolhas e avance no jogo
}

// Inicie o jogo quando a página for carregada
window.onload = startGame;
