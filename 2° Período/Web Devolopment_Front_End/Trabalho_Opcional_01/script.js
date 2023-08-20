const gridRows = 5;
const gridCols = 10;
const maxShips = 40;
const ships = generateShips(maxShips);
let score = 0;
let life = 3;

function generateShips(numShips) {
    const generatedShips = [];
    for (let i = 0; i < numShips; i++) {
        const row = Math.floor(Math.random() * gridRows);
        const col = Math.floor(Math.random() * gridCols);
        generatedShips.push([row, col]);
    }
    return generatedShips;
}

function updateScoreAndLife(hit) {
    if (hit) {
        score += 100;
        document.getElementById("score").textContent = score;
    } else {
        life -= 1;
        document.getElementById("life").textContent = life;
        if (life === 0) {
            alert("Fim de jogo! O jogo será reiniciado.");
            location.reload();
        }
    }
}

function shipOnClick(row, col) {
    const cellId = `ship_${row}_${col}`;
    const cell = document.getElementById(cellId);

    if (isShipHit(row, col)) {
        cell.src = "navio.jpg";
        alert("Você encontrou um navio!");
        updateScoreAndLife(true);
    } else {
        cell.src = "mar.jpg";
        alert("Água! tente novamente.");
        updateScoreAndLife(false);
    }

    cell.onclick = null;
}

function isShipHit(row, col) {
    for (const ship of ships) {
        if (ship[0] === row && ship[1] === col) {
            return true;
        }
    }
    return false;
}

const grid = document.getElementById("grid");

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
