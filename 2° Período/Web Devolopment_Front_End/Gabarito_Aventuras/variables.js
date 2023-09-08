const map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
const hero = {
    'name': '',
    'life': 10,
    'atq': 5,
    'def': 3,
    'inv': {
        'heal': 2,
        'str': 0
    }
}

const directions_results = {
    '01' : {
        'n': 'Você bate com a cara na parede. Preste mais atenção!!!',
        's': 'Você bate com a cara na parede. Preste mais atenção!!!',
        'l': 'Você segue pelo corredor do castelo...',
        'o': 'Você é um tremendo covarde... suma daqui!!!'
    },
    '11' : {
        'n': 'Você bate com a cara na parede. Preste mais atenção!!!',
        's': 'Você bate com a cara na parede. Preste mais atenção!!!',
        'l': 'Você segue pelo corredor do castelo...',
        'o': 'Você volta pelo corredor do castelo...'
    }
}

const histories = {
    '01': 'Você está na entrada do castelo. No corredor de entrada o único caminho que pode seguir é em frente... ou voltar e ir embora. Para onde deseja ir?<br><br>Para seguir o corredor, vá para o LESTE<br><br>Para voltar e ir embora, vá para o OESTE',
    '11': 'Seguindo o corredor você morreu... huahahauhuah'
}

const mapImages = {
    '01': 'map.png',
    '11': 'corridor1.png'
}

let x = -1;
let y = -1;