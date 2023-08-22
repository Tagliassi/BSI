const gridRows = 8;
const gridCols = 12;
const maxShips = 25;
const ships = generateShips(maxShips);
let score = 0;
let life = 3;

// elementos DOM
const grid = document.getElementById("grid");
const button = document.getElementById("button");

function onChangeShotType(valor, row, col) {

    switch(parseInt(valor)) {
        case 1:
             isShipHit(row, col);
            console.log("chamou a primeira");
            break;

        case 2:
             isBombHit(5, 5);
            console.log("chamou a segunda");
            break;

        case 3:
            isAtomBombHit(row, col);
            console.log("chamou a terceira");
            break;

        default:
            break;
    }
}

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
})

function changeLife(newNumberLife){
    life = parseInt(newNumberLife);
    
    document.getElementById("life").textContent = life;
}

function onClickInitGame(){

    if(button.value == "Iniciar Jogo"){
        createCards();
        button.value = "Reiniciar jogo";
        button.classList.toggle("visible");
    }
    else{
        location.reload();
    }
    
}

// Atualize a função generateShips para incluir bombas e bombas atômicas
function generateShips(numShips) {
    const generatedShips = [];
    for (let i = 0; i < numShips; i++) {
        const row = Math.floor(Math.random() * gridRows);
        const col = Math.floor(Math.random() * gridCols);
        generatedShips.push([row, col]);

        // Adicione três submarinos em posições aleatórias
        for (let j = 0; j < 3; j++) {
            const subRow = Math.floor(Math.random() * gridRows);
            const subCol = Math.floor(Math.random() * gridCols);
            generatedShips.push([subRow, subCol]);
        }

        // Adicione uma bomba em uma posição aleatória
        const bombRow = Math.floor(Math.random() * gridRows);
        const bombCol = Math.floor(Math.random() * gridCols);
        generatedShips.push([bombRow, bombCol]);

        // Adicione uma bomba atômica em uma posição aleatória
        const atomBombRow = Math.floor(Math.random() * gridRows);
        const atomBombCol = Math.floor(Math.random() * gridCols);
        generatedShips.push([atomBombRow, atomBombCol]);
    }
    return generatedShips;
}

document.getElementById('checkbox').onclick = function() {
    var disabled = document.getElementById("disableMessages").disabled;
    if (disabled) {
        document.getElementById("disableMessages").disabled = false;
    }
    else {
        document.getElementById("disableMessages").disabled = true;
    }
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
            finishGame()
        }
    }
}

function activeAndInactiveButton(){
    const button = document.getElementById("button");
    button.classList.toggle("visible");
}

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

function isShipHit(row, col) {
    for (const ship of ships) {
        if (ship[0] === row && ship[1] === col) {
            return true;
        }
    }
    return false;
}

// Adicione a função isSubmarineHit
function isSubmarineHit(row, col) {
    for (const ship of ships) {
        if (ship[0] === row && ship[1] === col) {
            return true;
        }
    }
    return false;
}

function isBombHit(row, col) {
    for (const ship of ships) {
        if (ship[5] === row && ship[5] === col) {
            return true;
        }
    }
    return false;
}

function isAtomBombHit(row, col){
    for (const ship of ships){
        if (ship[3] === row && ship[3] === col ){
            return true;
        }
    }
    return false;
}

function createCards(){
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

function finishGame(){
    button.classList.toggle("visible");
    grid.classList.add("visible");
}
