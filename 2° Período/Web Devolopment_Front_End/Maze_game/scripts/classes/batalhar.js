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
          console.log(`${this.player.nome} causou ${danoDoPlayer} de dano ao monstro.`);
  
          if (this.monstro.vida <= 0) {
            console.log(`${this.player.nome} ganhou a batalha!, continue explorando`);
          }
        } else {
          // Monstro ataca o player
          const danoDoMonstro = this.monstro.dano;
          this.player.vida -= danoDoMonstro;
          console.log(`O monstro causou ${danoDoMonstro} de dano a ${this.player.nome}.`);
  
          if (this.player.vida <= 0) {
            console.log(`${this.player.nome} perdeu a batalha!`);
            window.onload = startGame;
          }
        }
      }
    }
}
  