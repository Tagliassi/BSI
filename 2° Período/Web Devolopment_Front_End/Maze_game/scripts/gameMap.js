// Classe GameMap
class GameMap {
  constructor() {
      // Definir mapa bidimensional
      this.map = [
          [
              new Localizacao("0", "Você está na localização [0][0]."),
              new Localizacao("1", "Você está na localização [0][1]."),
              new Localizacao("2", "Você está na localização [0][2]."),
              new Localizacao("3", "Você está na localização [0][3]."), 
              new Localizacao("4", "Você está na localização [0][4]."), 
              new Localizacao("5", "Você está na localização [0][5]."), 
              new Localizacao("6", "Você está na localização [0][6]."), 
              new Localizacao("7", "Você está na localização [0][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [1][0]."),
              new Localizacao("1", "Você está na localização [1][1]."),
              new Localizacao("2", "Você está na localização [1][2]."),
              new Localizacao("3", "Você está na localização [1][3]."), 
              new Localizacao("4", "Você está na localização [1][4]."), 
              new Localizacao("5", "Você está na localização [1][5]."), 
              new Localizacao("6", "Você está na localização [1][6]."), 
              new Localizacao("7", "Você está na localização [1][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [2][0]."),
              new Localizacao("1", "Você está na localização [2][1]."),
              new Localizacao("2", "Você está na localização [2][2]."),
              new Localizacao("3", "Você está na localização [2][3]."), 
              new Localizacao("4", "Você está na localização [2][4]."), 
              new Localizacao("5", "Você está na localização [2][5]."), 
              new Localizacao("6", "Você está na localização [2][6]."), 
              new Localizacao("7", "Você está na localização [2][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [3][0]."),
              new Localizacao("1", "Você está na localização [3][1]."),
              new Localizacao("2", "Você está na localização [3][2]."),
              new Localizacao("3", "Você está na localização [3][3]."), 
              new Localizacao("4", "Você está na localização [3][4]."), 
              new Localizacao("5", "Você está na localização [3][5]."), 
              new Localizacao("6", "Você está na localização [3][6]."), 
              new Localizacao("7", "Você está na localização [3][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [4][0]."),
              new Localizacao("1", "Você está na localização [4][1]."),
              new Localizacao("2", "Você está na localização [4][2]."),
              new Localizacao("3", "Você está na localização [4][3]."), 
              new Localizacao("4", "Você está na localização [4][4]."), 
              new Localizacao("5", "Você está na localização [4][5]."), 
              new Localizacao("6", "Você está na localização [4][6]."), 
              new Localizacao("7", "Você está na localização [4][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [5][0]."),
              new Localizacao("1", "Você está na localização [5][1]."),
              new Localizacao("2", "Você está na localização [5][2]."),
              new Localizacao("3", "Você está na localização [5][3]."), 
              new Localizacao("4", "Você está na localização [5][4]."), 
              new Localizacao("5", "Você está na localização [5][5]."), 
              new Localizacao("6", "Você está na localização [5][6]."), 
              new Localizacao("7", "Você está na localização [5][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [6][0]."),
              new Localizacao("1", "Você está na localização [6][1]."),
              new Localizacao("2", "Você está na localização [6][2]."),
              new Localizacao("3", "Você está na localização [6][3]."), 
              new Localizacao("4", "Você está na localização [6][4]."), 
              new Localizacao("5", "Você está na localização [6][5]."), 
              new Localizacao("6", "Você está na localização [6][6]."), 
              new Localizacao("7", "Você está na localização [6][7].")
          ],
          [
              new Localizacao("0", "Você está na localização [7][0]."),
              new Localizacao("1", "Você está na localização [7][1]."),
              new Localizacao("2", "Você está na localização [7][2]."),
              new Localizacao("3", "Você está na localização [7][3]."), 
              new Localizacao("4", "Você está na localização [7][4]."), 
              new Localizacao("5", "Você está na localização [7][5]."), 
              new Localizacao("6", "Você está na localização [7][6]."), 
              new Localizacao("7", "Você está na localização [7][7].")
          ],
      ];

      this.LocalizacaoAtual = this.map[0][0]; // Comece na primeira localização
  }

  // Método para mover o jogador para uma localização específica
  movePersonagem(x, y) {
      if (x >= 0 && x < this.map.length && y >= 0 && y < this.map[0].length) {
          this.LocalizacaoAtual = this.map[x][y];
      }
  }
  
}