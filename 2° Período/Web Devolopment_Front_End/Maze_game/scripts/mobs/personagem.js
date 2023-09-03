class Personagem {
    constructor(nome) {
        this.nome = nome;
        this.vida = 3;
        this.dano = 10;
        this.defesa = 0;
        this.inventario = [];
    }

    // Método para atualizar os corações com base na vida atual do jogador
    atualizarCoracoes() {
        const heartsContainer = document.querySelector('.hearts');

        // Remova todos os corações existentes
        heartsContainer.innerHTML = '';

        // Crie corações com base na vida atual
        for (let i = 0; i < this.vida; i++) {
            const heart = document.createElement('div');
            heart.classList.add('heart');
            heartsContainer.appendChild(heart);
        }
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