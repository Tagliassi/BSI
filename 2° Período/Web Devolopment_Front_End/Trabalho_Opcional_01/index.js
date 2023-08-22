const gridRows = 8;
const gridCols = 12;

const WATER = 0;
const SUBMARINE = 1;
const BOMB = 2;
const ATOMIC_BOMB = 3;
const SHIP = 4;

const shipScores = {
    [SUBMARINE]: 50,       // Pontuação para submarinos
    [BOMB]: 0,          // Pontuação para bombas
    [ATOMIC_BOMB]: 0,   // Pontuação para bombas atômicas
    [SHIP]: 20,            // Pontuação para navios
};

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

const grid = document.getElementById("grid");
const scoreElement = document.getElementById("score");
const lifeElement = document.getElementById("life");

let score = 0;
let life = 3;

const ships = [];

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

function placeShipRandomly(shipType) {
    let row, col;
    do {
        row = Math.floor(Math.random() * gridRows);
        col = Math.floor(Math.random() * gridCols);
    } while (ships[row][col] !== WATER);

    ships[row][col] = shipType;
}

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

// Função para atualizar as vidas no jogo
function updateLives(lives) {
    const lifeSpan = document.getElementById("life");
    lifeSpan.textContent = lives;
}

// Inicializa a quantidade de vidas
updateLives(3); // Defina o valor inicial das vidas aqui

function finishGame() {
    // Coloque aqui o código para reiniciar o jogo, como resetar as variáveis de pontuação, vidas e cartas clicadas.
    score = 0;
    document.getElementById("score").textContent = score;
    life = 3;
    clickedCards.clear(); // Limpar as cartas clicadas

    // Também é necessário restaurar as imagens das cartas para o estado inicial (imagem de carta virada para baixo).
    const allCards = document.getElementsByTagName("img");
    for (const card of allCards) {
        card.src = "carta.jpg";
    }

    // Aqui você pode chamar a função que gera os navios e faz o embaralhamento novamente.
    generateShips();
    shuffle();
}

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

function onClickInitGame() {
    if (button.value == "Iniciar Jogo") {
        generateShips();
        shuffle();
        createCards();
        button.value = "Reiniciar jogo";
        button.classList.toggle("visible");
    } else {
        location.reload();
    }
}

const clickedCards = new Set(); // Keep track of already clicked cards

function shipOnClick(row, col) {
    const card = document.getElementById(`ship_${row}_${col}`);

    // Check if the card has already been clicked
    if (clickedCards.has(card)) {
        return;
    }

    clickedCards.add(card); // Mark the card as clicked

    const shipType = ships[row][col];

    if (shipType === WATER) {
        card.src = getImage(WATER);
        updateScoreAndLife(false);
    } else {
        card.src = getImage(shipType);
        updateScoreAndLife(true, shipType); // Passar o tipo de navio clicado
        if (!document.getElementById("chkDisable").checked) {
            const shipName = shipNames[shipType];
            alert(`Você encontrou um ${shipName}!`);
        }
    }
}


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




