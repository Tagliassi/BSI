// Classe Portal
export class Portal {
  constructor(nome) {
    this.nome = nome;
  }

  teleportarPersonagemAleatoriamente(personagem, mapa) {
    // Implementar a lógica de teleportação aqui
    const larguraDoMapa = mapa.map[0].length;
    const alturaDoMapa = mapa.map.length;

    // Gerar coordenadas aleatórias
    const x = Math.floor(Math.random() * alturaDoMapa);
    const y = Math.floor(Math.random() * larguraDoMapa);

    // Mover o personagem para as novas coordenadas
    personagem.movePersonagem(x, y);

    console.log(`O personagem foi teletransportado aleatoriamente para (${x}, ${y}).`);
  }

  verificarSeTemPortal(personagem) {
    const localizacaoAtual = personagem.obterLocalizacaoExata();

    if (localizacaoAtual.x === 6 && localizacaoAtual.y === 3) {
      console.log("O personagem encontrou um portal e foi teletransportado aleatoriamente pelo mapa.");
      this.teleportarPersonagemAleatoriamente(personagem, personagem.mapa);
    }
  }
}
