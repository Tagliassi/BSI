import { alterarFundo } from './alterGameInterface.js';
import { alterarTexto } from './alterGameInterface.js';

// Função para atualizar a interface do jogo
function updateGameInterface() {
    // Implemente a lógica para atualizar a interface do jogo aqui
    alterarFundo('./../assets/cenario/corpo-morto.png');
    alterarTexto("blablablal");
}
updateGameInterface();
// Função para iniciar o jogo
function startGame() {
    const playerName = prompt("Qual é o seu nome?");
    const player = new Personagem(playerName);
    player.atualizarCoracoes();
    const gameMap = new GameMap();

    // Inicialize a interface do jogo
    updateGameInterface();

    // Implemente o loop do jogo aqui, permitindo que o jogador faça escolhas e avance no jogo
}

// Inicie o jogo quando a página for carregada
window.onload = startGame;
