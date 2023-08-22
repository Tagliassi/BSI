const gridRows = 8;
const gridCols = 12;
const maxShips = 25;
const ships = generateShips(maxShips);
let score = 0;
let life = 3;

const grid = document.getElementById("grid");
const button = document.getElementById("button");

// Attach event listener for life selection
const elemento = document.getElementById("lifeSelected");
elemento.addEventListener("click", (e) => {
    var selectedValue = "";
    var radioButtons = document.getElementsByName("level");
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            selectedValue = radioButtons[i].value;
            break;
        }
    }
    changeLife(parseInt(selectedValue));
});

// Toggle message disable checkbox
document.getElementById('checkbox').onclick = function() {
    var disabled = document.getElementById("disableMessages").disabled;
    document.getElementById("disableMessages").disabled = !disabled;
};

// Initialize the game
function onClickInitGame() {
    if (button.value == "Iniciar Jogo") {
        createCards();
        button.value = "Reiniciar jogo";
        button.classList.toggle("visible");
    } else {
        location.reload();
    }
}

// Generate ships and bombs
function generateShips(numShips) {
    const generatedShips = [];
    for (let i = 0; i < numShips; i++) {
        // Generate ship
        const shipRow = Math.floor(Math.random() * gridRows);
        const shipCol = Math.floor(Math.random() * gridCols);
        generatedShips.push([shipRow, shipCol]);

        // Generate submarines
        for (let j = 0; j < 3; j++) {
            const subRow = Math.floor(Math.random() * gridRows);
            const subCol = Math.floor(Math.random() * gridCols);
            generatedShips.push([subRow, subCol]);
        }

        // Generate bomb
        const bombRow = Math.floor(Math.random() * gridRows);
        const bombCol = Math.floor(Math.random() * gridCols);
        generatedShips.push([bombRow, bombCol]);

        // Generate atomic bomb
        const atomBombRow = Math.floor(Math.random() * gridRows);
        const atomBombCol = Math.floor(Math.random() * gridCols);
        generatedShips.push([atomBombRow, atomBombCol]);
    }
    return generatedShips;
}

// Update score and life
function updateScoreAndLife(hit) {
    if (hit) {
        score += 100;
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

// Handle ship click
function shipOnClick(row, col) {
    
    let cellId = "";

    const selectedButton = document.getElementById("select-button");

    let selectedIndex = selectedButton.selectedIndex;
    let selectedValue = selectedButton.options[selectedIndex].value;

    switch(parseInt(selectedValue)) {
        case 1:
            // normal
            cellId = `ship_${row}_${col}`;
            break;

        case 2:
            cellId = `ship_${row}_${col}`;
            break;

        case 3:
            cellId = `ship_${row}_${col}`;
            break;

        default:
            break;
    }

    const cell = document.getElementById(cellId);

    if (isShipHit(row, col)) {
        cell.src = "navio.jpg";
        alert("Você encontrou um navio!");
        updateScoreAndLife(true);
    } else if (isSubmarineHit(row, col)) {
        cell.src = "submarino.jpg";
        alert("Você encontrou um submarino!");
        updateScoreAndLife(true);
    } else if (isBombHit(row, col)) {
        cell.src = "bomba.jpg";
        alert("Você encontrou uma bomba!");
        updateScoreAndLife(false);
    } else if (isAtomBombHit(row, col)) {
        cell.src = "bomba_atomica.jpg";
        alert("Você encontrou uma bomba atômica!");
        updateScoreAndLife(false);
    } else {
        cell.src = "mar.jpg";
        alert("Água! Tente novamente.");
        updateScoreAndLife(false);
    }

    cell.onclick = null;
}

// Check if a ship was hit
function isShipHit(row, col) {
    for (const ship of ships) {
        if (ship[0] === row && ship[1] === col) {
            return true;
        }
    }
    return false;
}

// Check if a submarine was hit
function isSubmarineHit(row, col) {
    for (const ship of ships) {
        if (ship[0] === row && ship[1] === col) {
            return true;
        }
    }
    return false;
}
// Check if a bomb was hit
function isBombHit(row, col) {
    for (const ship of ships) {
        if (ship[1] === row && ship[2] === col) {
            return true;
        }
    }
    return false;
}

// Check if an atomic bomb was hit
function isAtomBombHit(row, col) {
    for (const ship of ships){
        if (ship[3] === row && ship[4] === col ){
            return true;
        }
    }
    return false;
}

// Create the grid cards
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

// Finish the game
function finishGame() {
    button.classList.toggle("visible");
    grid.classList.add("visible");
}
