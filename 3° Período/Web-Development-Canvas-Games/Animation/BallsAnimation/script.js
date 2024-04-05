const ball1 = document.getElementById('ball1');
const ball2 = document.getElementById('ball2');

const getRandomDirection = () => Math.random() > 0.5 ? 1 : -1;

let ball1DirectionX = getRandomDirection();
let ball1DirectionY = getRandomDirection();
let ball2DirectionX = getRandomDirection();
let ball2DirectionY = getRandomDirection();

const moveBall = (ball, directionX, directionY) => {
  const ballRect = ball.getBoundingClientRect();

  if (ballRect.top <= 0 || ballRect.bottom >= window.innerHeight) {
    directionY *= -1;
  }

  if (ballRect.left <= 0 || ballRect.right >= window.innerWidth) {
    directionX *= -1;
  }

  ball.style.top = ballRect.top + directionY + 'px';
  ball.style.left = ballRect.left + directionX + 'px';

  return [directionX, directionY];
};

setInterval(() => {
  [ball1DirectionX, ball1DirectionY] = moveBall(ball1, ball1DirectionX, ball1DirectionY);
  [ball2DirectionX, ball2DirectionY] = moveBall(ball2, ball2DirectionX, ball2DirectionY);
}, 10);
