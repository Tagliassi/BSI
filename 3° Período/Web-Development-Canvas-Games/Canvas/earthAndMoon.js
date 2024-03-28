const toRad = (angDeg) => angDeg * Math.PI / 180;

/**
 * Desenha a lua. Note que consideramos a terra como se estivesse na posição 0,0.
 * @param ctx Contexto gráfico onde o desenho ocorrerá
 * @param angle angulo em relação à terra
 */
function moon(ctx, angle) {
    ctx.save();
    ctx.beginPath()
    ctx.rotate(angle)     //Rodamos o sistema de coordenadas em angle graus
    ctx.translate(150, 0) //E afastamos 150 em x nesse eixo rotacionado

    //Desenhamos a lua
    ctx.fillStyle = "#e5e4e2"
    ctx.arc(0, 0, 20, 0, 2 * Math.PI);
    ctx.fill()
    ctx.stroke()
    ctx.restore()
}

/**
 * Desenha a terra na posição 0,0
 * Ela irá comandar o desenho da lua em seu próprio sistema coordenado
 * @param ctx O contexto gráfico
 */
function earth(ctx) {
    ctx.save()
    ctx.beginPath()
    ctx.fillStyle = "#1111d9"
    ctx.arc(0, 0, 40, 0, 2 * Math.PI);
    ctx.fill()
    ctx.stroke()
    moon(ctx, toRad(110))
    ctx.restore()
}

function draw(ctx) {
    ctx.save()
    ctx.lineWidth = 2
    ctx.strokeStyle = "black"

    //Posicionamos o sistema coordenado na posição 200,200
    ctx.translate(200, 200)
    earth(ctx)  //Desenhamos o planeta Terra
    ctx.restore()
}

const canvas = document.querySelector('#canvas');
if (!canvas.getContext) {
    alert("Canvas não disponível!")
} else {
    draw(canvas.getContext('2d'));
}
