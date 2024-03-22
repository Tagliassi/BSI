function draw(ctx) {
    // Desenhar o mar
    ctx.fillStyle = "blue";
    ctx.fillRect(0, 0, 400, 400);

    // Desenhar a lua
    ctx.beginPath();
    ctx.fillStyle = "yellow";
    ctx.arc(350, 50, 30, 0, Math.PI * 2);
    ctx.fill();

    // Desenhar o peixe laranja
    ctx.fillStyle = "orange";
    ctx.beginPath();
    ctx.moveTo(200, 150); // cabeça
    ctx.lineTo(220, 160); // nadadeira superior
    ctx.lineTo(220, 140); // nadadeira inferior
    ctx.closePath();
    ctx.fill();
    ctx.beginPath();
    ctx.arc(200, 150, 10, 0, Math.PI * 2); // corpo
    ctx.fill();
    ctx.beginPath();
    ctx.arc(210, 150, 2, 0, Math.PI * 2); // olho
    ctx.fillStyle = "black";
    ctx.fill();

    // Desenhar o peixe azul
    ctx.fillStyle = "red";
    ctx.beginPath();
    ctx.moveTo(50, 250); // cabeça
    ctx.lineTo(70, 260); // nadadeira superior
    ctx.lineTo(70, 240); // nadadeira inferior
    ctx.closePath();
    ctx.fill();
    ctx.beginPath();
    ctx.arc(50, 250, 10, 0, Math.PI * 2); // corpo
    ctx.fill();
    ctx.beginPath();
    ctx.arc(60, 250, 2, 0, Math.PI * 2); // olho
    ctx.fillStyle = "black";
    ctx.fill();

    // Desenhar o peixe verde
    ctx.fillStyle = "green";
    ctx.beginPath();
    ctx.moveTo(300, 300); // cabeça
    ctx.lineTo(320, 310); // nadadeira superior
    ctx.lineTo(320, 290); // nadadeira inferior
    ctx.closePath();
    ctx.fill();
    ctx.beginPath();
    ctx.arc(300, 300, 10, 0, Math.PI * 2); // corpo
    ctx.fill();
    ctx.beginPath();
    ctx.arc(310, 300, 2, 0, Math.PI * 2); // olho
    ctx.fillStyle = "black";
    ctx.fill();
}

const canvas = document.querySelector('#canvas');
if (!canvas.getContext) {
    alert("Canvas não disponível!")
} else {
    draw(canvas.getContext('2d'));
}
