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

  verificarSeTemPorta() {
    const localizacaoAtual = this.obterLocalizacaoExata();

    if (
      (localizacaoAtual.x === 3 && localizacaoAtual.y === 2) ||
      (localizacaoAtual.x === 5 && localizacaoAtual.y === 5)
    ) {
      console.log(`O personagem encontrou uma porta (${this.nome}).`);

      if (this.trancada) {
        console.log(`Esta porta está trancada e requer uma chave.`);
        const chaveNoInventario = this.verificarChaveNoInventario();
        
        if (chaveNoInventario) {
          this.abrirPorta(chaveNoInventario);
          console.log(`O personagem destrancou a porta ${this.nome}, continue explorando.`);
        } else {
          console.log(`Você precisa encontrar a chave certa para abrir a porta ${this.nome}.`);
        }
      } else {
        console.log(`Esta porta já está destrancada, continue explorando.`);
      }
    }
  }

  verificarChaveNoInventario() {
    for (const item of this.inventario) {
      if (item instanceof Chave && item.tipoDeChave === this.tipoDeChave) {
        return item;
      }
    }
    return null;
  }
}
