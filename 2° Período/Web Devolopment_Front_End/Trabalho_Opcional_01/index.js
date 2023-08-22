// Constants
const gridRows = 8;
const gridCols = 12;

const WATER = 0;
const SUBMARINE = 1;
const BOMB = 2;
const ATOMIC_BOMB = 3;
const SHIP = 4;

const shipScores = {
    [SUBMARINE]: 50,       
    [SHIP]: 20,            
};

let regularBombsStock = 1;
let atomicBombsStock = 1;
const maxRegularBombs = 2; 
const maxAtomicBombs = 2; 

const shipNames = {
    [SUBMARINE]: "Submarino",
    [BOMB]: "Bomba",
    [ATOMIC_BOMB]: "Bomba Atômica",
    [SHIP]: "Navio",
};

const shipCounts = {
    [SUBMARINE]: 10,
    [BOMB]: 1,
    [ATOMIC_BOMB]: 1,
    [SHIP]: 40,
};

// HTML Elements
const grid = document.getElementById("grid");
const scoreElement = document.getElementById("score");
const lifeElement = document.getElementById("life");

// Game State
let score = 0;
let life = 3;
const ships = [];
const clickedCards = new Set();

// Initialize the game
function onClickInitGame() {
    if (button.value == "Iniciar Jogo") {
        generateShips();
        shuffle();
        createCards();
        button.value = "Reiniciar jogo";
        button.classList.toggle("visible");
        const container02 = document.getElementById("button");
        container02.style.display = "none";
        const levelRadios = document.getElementsByName("level");
        for (const radio of levelRadios) {
            radio.disabled = true;
        }

    } else {
        location.reload();
    }
}

//return the images for each type of object
function getImage(type) {
    switch (type) {
        case WATER:
            return "mar.jpg";
        case SUBMARINE:
            return "submarino.jpg";
        case BOMB:
            return "bomba.jpg";
        case ATOMIC_BOMB:
            return "bomba_atomica.jpg";
        case SHIP:
            return "navio.jpg";
        default:
            return "carta.jpg";
    }
}

// Create the game grid
function createCards() {
    for (let i = 0; i < gridRows; i++) {
        const row = document.createElement("tr");
        for (let j = 0; j < gridCols; j++) {
            const cell = document.createElement("td");
            const img = document.createElement("img");
            img.src = "carta.jpg";
            img.id = `ship_${i}_${j}`;
            img.addEventListener("click", () => shipOnClick(i, j));
            cell.appendChild(img);
            row.appendChild(cell);
        }
        grid.appendChild(row);
    }
}

// Generate the initial ship placements
function generateShips() {
    for (let i = 0; i < gridRows; i++) {
        ships.push([]);
        for (let j = 0; j < gridCols; j++) {
            ships[i][j] = WATER;
        }
    }

    for (const shipType in shipCounts) {
        for (let count = 0; count < shipCounts[shipType]; count++) {
            placeShipRandomly(parseInt(shipType));
        }
    }
}

// Place a ship randomly on the grid
function placeShipRandomly(shipType) {
    let row, col;
    do {
        row = Math.floor(Math.random() * gridRows);
        col = Math.floor(Math.random() * gridCols);
    } while (ships[row][col] !== WATER);

    ships[row][col] = shipType;
}

// Shuffle the ship placements
function shuffle() {
    for (let i = 0; i < 1000; i++) {
        let i1 = Math.floor(Math.random() * 8);
        let j1 = Math.floor(Math.random() * 12);
        let i2 = Math.floor(Math.random() * 8);
        let j2 = Math.floor(Math.random() * 12);
        let temp = ships[i1][j1];
        ships[i1][j1] = ships[i2][j2];
        ships[i2][j2] = temp;
    }
}

// Shot setup
let shotType = "simple";

// Receive the type of shot chosen
document.getElementById("select-button").addEventListener("change", function(event) {
    shotType = event.target.value;
});


function shipOnClick(row, col) {
    const card = document.getElementById(`ship_${row}_${col}`);

    // Check if the card has already been clicked
    if (clickedCards.has(card)) {
        return;
    }

    // Check if the player has used the maximum number of regular bombs
    if (shotType === "bomb" && regularBombsStock >= maxRegularBombs) {
        alert("You've used all your regular bombs!");
        return;
    }

    // Check if the player has used the maximum number of atomic bombs
    if (shotType === "atomic_bomb" && atomicBombsStock >= maxAtomicBombs) {
        alert("You've used all your atomic bombs!");
        return;
    }

    // Mark the card as clicked
    clickedCards.add(card); 

    const shipType = ships[row][col];

    if (shipType === WATER) {
        card.src = getImage(WATER);
        updateScoreAndLife(false);
    } else {
        card.src = getImage(shipType);
        updateScoreAndLife(true, shipType); 
        if (!document.getElementById("chkDisable").checked) {
            const shipName = shipNames[shipType];
            alert(`Você encontrou um ${shipName}!`);
        }
    }
        // Verificar se é uma bomba regular
        if (shipType === BOMB) {
            regularBombsStock++;
            if (regularBombsStock > maxRegularBombs) {
                regularBombsStock = maxRegularBombs;
            }
        }
        // Verificar se é uma bomba atômica
        if (shipType === ATOMIC_BOMB) {
            atomicBombsStock++;
            if (atomicBombsStock > maxAtomicBombs) {
                atomicBombsStock = maxAtomicBombs;
            }
        }

    if (shotType === "simple") {
        revealTile(row, col);
    } else if (shotType === "bomb") {
        revealTilesInCross(row, col);
    } else if (shotType === "atomic_bomb") {
        revealTilesInSquare(row, col);
    }
}

// Functions to reveal tiles based on shot types
function revealTile(row, col) {
    const revealSingleTile = (r, c) => {
        const currentCard = document.getElementById(`ship_${r}_${c}`);
        if (!clickedCards.has(currentCard)) {
            clickedCards.add(currentCard);
            const shipType = ships[r][c];
            currentCard.src = getImage(shipType);
            updateScoreAndLife(shipType !== WATER, shipType);
        }
    };
    revealSingleTile(row, col);
}

function revealTilesInCross(row, col) {
    const revealSingleTile = (r, c) => {
        const currentCard = document.getElementById(`ship_${r}_${c}`);
        if (!clickedCards.has(currentCard)) {
            clickedCards.add(currentCard);
            const shipType = ships[r][c];
            currentCard.src = getImage(shipType);
            updateScoreAndLife(shipType !== WATER, shipType);
        }
        // Increment the regular bombs used if the shot type is bomb
        if (shotType === "bomb") {
            regularBombsStock--;
            if (regularBombsStock < 0) {
                regularBombsStock = 0;
            }
        }
    };

    revealSingleTile(row, col); // Reveal the center tile

    // Reveal tiles in cross pattern (up, down, left, right)
    for (let offset of [-1, 1]) {
        revealSingleTile(row + offset, col);
        revealSingleTile(row, col + offset);
    }
}

function revealTilesInSquare(row, col) {
    const revealSingleTile = (r, c) => {
        const currentCard = document.getElementById(`ship_${r}_${c}`);
        if (!clickedCards.has(currentCard)) {
            clickedCards.add(currentCard);
            const shipType = ships[r][c];
            currentCard.src = getImage(shipType);
            updateScoreAndLife(shipType !== WATER, shipType);
        }
        // Increment the atomic bombs used if the shot type is atomic_bomb
        if (shotType === "atomic_bomb") {
            atomicBombsStock--;
            if (atomicBombsStock < 0) {
                atomicBombsStock = 0;
            }
        }
    };

    // Reveal tiles in a square pattern (3x3 grid)
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            revealSingleTile(row + i, col + j);
        }
    }
}

// Update the score and life based on a hit or miss
function updateScoreAndLife(hit, shipType) {
    if (hit) {
        score += shipScores[shipType]; // Usar a tabela de pontuações
        document.getElementById("score").textContent = score;
    } else {
        life -= 1;
        document.getElementById("life").textContent = life;
        if (life === 0) {
            alert("Fim de jogo! O jogo será reiniciado.");
            finishGame();
        }
    }
}

// Handle the life selection radio button click
// Função para lidar com o clique no botão "Selecionar"
function handleLifeSelection() {
    const levelRadios = document.getElementsByName("level");

    let selectedLevel;
    for (const radio of levelRadios) {
        if (radio.checked) {
            selectedLevel = parseInt(radio.value);
            break;
        }
    }

    if (selectedLevel === 3 || selectedLevel === 5 || selectedLevel === 7) {
        updateLives(selectedLevel);
    } else {
        console.log("Nível de vidas inválido.");
    }
}

document.getElementById("lifeSelected").addEventListener("click", handleLifeSelection);

// Update the displayed life count
function updateLives(lives) {
    life = lives;
    const lifeSpan = document.getElementById("life");
    lifeSpan.textContent = life;
}

function resetBombCounters() {
    regularBombsStock = 1;
    atomicBombsStock = 1;
}

// Finish the game and reset everything
function finishGame() {
    // Coloque aqui o código para reiniciar o jogo, como resetar as variáveis de pontuação, vidas e cartas clicadas.
    score = 0;
    document.getElementById("score").textContent = score;
    life = 3;
    clickedCards.clear(); // Limpar as cartas clicadas
    resetBombCounters()

    // Também é necessário restaurar as imagens das cartas para o estado inicial (imagem de carta virada para baixo).
    const allCards = document.getElementsByTagName("img");
    for (const card of allCards) {
        card.src = "carta.jpg";
    }

    // Aqui você pode chamar a função que gera os navios e faz o embaralhamento novamente.
    const container02 = document.getElementById("button");
    container02.style.display = "block";
    grid.innerHTML = ""; 
    generateShips();
    shuffle();
}

// Initial setup for lives display
updateLives(3);
