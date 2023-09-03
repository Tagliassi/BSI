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