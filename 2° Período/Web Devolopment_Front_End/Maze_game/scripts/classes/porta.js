// Classe Porta
export class Porta {
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

  verificarSeTemPorta(){
    if (this.player.posicaoAtual[0] === 3 && this.player.posicaoAtual[1] === 2 || this.player.posicaoAtual[0] === 5 && this.player.posicaoAtual[1] === 5) {
      console.log("O personagem encontrou uma porta, precisa de chave para abri-la.");
      //verificar se a chave especifica dessa porta esta no inventario, se tiver abre a porta.
      abrirPorta(chave)
      console.log("O personagem encontrou abriu a porta, continue explorando.");
    }
  }
}