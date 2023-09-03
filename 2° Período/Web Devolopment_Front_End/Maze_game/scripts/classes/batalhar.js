class Batalha {
    constructor(player, monstro) {
        this.player = player;
        this.monstro = monstro;
    }

    batalhar() {
        while (this.player.vida > 0 && this.monstro.vida > 0) {
            // Gerar um número aleatório para determinar quem ataca primeiro (1 para player, 0 para monstro)
            const quemAtacaPrimeiro = Math.random() < 0.5 ? 1 : 0;

            if (quemAtacaPrimeiro === 1) {
                // Player ataca o monstro
                const danoDoPlayer = this.player.dano;
                this.monstro.vida -= danoDoPlayer;
                console.log(`Você causou ${danoDoPlayer} de dano ao monstro.`);

                if (this.monstro.vida <= 0) {
                    console.log("Você ganhou a batalha!, continue explorando");
                }
            } 
            
            else {
                // Monstro ataca o player
                const danoDoMonstro = this.monstro.dano;
                this.player.vida -= danoDoMonstro;
                console.log(`O monstro causou ${danoDoMonstro} de dano a você.`);

                if (this.player.vida <= 0) {
                    console.log("Você perdeu a batalha!");
                    window.onload = startGame;
                }
            }
        }
    }

    iniciarBatalha(){
        // se a posição atual do player for igual a posição do monstro, inicia batalha
        if (this.player.posicaoAtual[0] === 1 && this.player.posicaoAtual[1] === 5) {
            console.log("O personagem encontra o monstro Creeper, a batalha inicia.");
            this.batalhar() 
        }
        // se a posição atual do player for igual a posição do monstro, inicia batalha
        else if (this.player.posicaoAtual[0] === 3 && this.player.posicaoAtual[1] === 1) {
            console.log("O personagem encontra o monstro Maicris, a batalha inicia.");
            this.batalhar() 
        }
        // se a posição atual do player for igual a posição do monstro, inicia batalha
        else if (this.player.posicaoAtual[0] === 3 && this.player.posicaoAtual[1] === 6) {
            console.log("O personagem encontra o monstro Capivara locona, a batalha inicia.");
            this.batalhar()
        }
        // se a posição atual do player for igual a posição do monstro, inicia batalha
        else if (this.player.posicaoAtual[0] === 5 && this.player.posicaoAtual[1] === 3) {
            console.log("O personagem encontra o monstro Moscona, a batalha inicia.");
            this.batalhar()
        }
        else {console.log("Não tem monstro")}
    }
}
