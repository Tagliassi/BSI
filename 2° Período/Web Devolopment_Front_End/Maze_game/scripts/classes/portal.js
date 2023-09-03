// Classe Portal
export class Portal {
  constructor(nome) {
      this.nome = nome;
  }

  teleportarPersonagemAleatoriamente() {
      // Implementar a lógica de teleportação aqui
  }

  verificarSeTemPortal(){
    if (this.player.posicaoAtual[0] === 6 && this.player.posicaoAtual[1] === 3) {
      console.log("O personagem encontrou um portal e foi teletransportado aleatoriamente pelo mapa.");
      teleportarPersonagemAleatoriamente()
    }
  }

}
