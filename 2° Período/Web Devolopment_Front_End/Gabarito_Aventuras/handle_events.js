function cmdUpOnClick() {
    if (x == -1) {
        verifyStart(true);
    }
    else {
        showResults(x, y-1, 'n');
    }
}

function cmdRightClick() {
    if (x == -1) {
        verifyStart(false);
    }
    else {
        showResults(x+1, y, 'l');
    }
}

function cmdDownClick() {
    if (x == -1) {
        verifyStart(false);
    }
    else {
        showResults(x, y+1, 's');
    }
}

function cmdLeftClick() {
    if (x == -1) {
        verifyStart(false);
    }
    else {
        showResults(x-1, y, 'o');
    }
}

function changeInfo() {
    let textarea = document.getElementById('textarea');
    let imagearea = document.getElementById('imagearea');
    
    textarea.innerHTML = histories[`${x}${y}`];
    imagearea.src = "images/" + mapImages[`${x}${y}`];
}

function showResults(newX, newY, dir) {
    alert(directions_results[`${x}${y}`][dir]);
    if (newX != -1 || newY != -1) {
        switch (map[newY][newX]) {
            case 0:
                hero.life--;
                break;
            case 1:
                x = newX;
                y = newY;
                changeInfo();
                break;
        }
    }
}

function verifyStart(up) {
    let textarea = document.getElementById('textarea');
    
    if (up) {
        x = 0;
        y = 1;
        textarea.innerHTML = histories[`${x}${y}`];
    }
    else {
        textarea.innerHTML = 'Você é um tremendo covarde... suma daqui!!!';
    }
}