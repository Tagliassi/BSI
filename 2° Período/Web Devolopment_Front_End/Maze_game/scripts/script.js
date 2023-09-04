import { alterarFundo } from "./alterGameInterface.js";
import { alterarTexto } from "./alterGameInterface.js";
import { Personagem } from "./mobs/personagem.js";
import { GameMap } from "./gameMap.js";


// Função para iniciar o jogo
function startGame() {
  const playerName = prompt("Qual é o seu nome?");

  if (playerName == null || playerName == "") {
    alert("Insira um nome válido.");
    location.reload();
  }

  // Cria Mapa
  const gameMap = new GameMap();

  // Cria personagem
  const player = new Personagem(playerName, gameMap);

  // Seta informações padrões
  alterarTexto(
    `Você acordou sozinho e com frio. Explore e encontre a saída do Labirinto!\n\n- ${player.apresentar()}`
  );

  ativarEventosPagina(player);
  player.atualizarCoracoes();

  // Inicialize a interface do jogo
  // Implemente o loop do jogo aqui, permitindo que o jogador faça escolhas e avance no jogo
}

function ativarEventosPagina(player) {
  document.getElementById("move-left").addEventListener("click", () => {
    player.moveEsquerda();
  });

  document.getElementById("move-up").addEventListener("click", () => {
    player.moveCima();
  });

  document.getElementById("move-down").addEventListener("click", () => {
    player.moveBaixo();
  });

  document.getElementById("move-right").addEventListener("click", () => {
    player.moveDireita();
  });
}
// Inicie o jogo quando a página for carregada
window.onload = startGame;
