// reflex.js

const starsContainer = document.querySelector('.stars');
for(let i=0; i<100; i++) {
  const star = document.createElement('div');
  star.className = 'star';
  star.style.top = Math.random()*100 + 'vh';
  star.style.left = Math.random()*100 + 'vw';
  star.style.width = star.style.height = (Math.random()*2+1) + 'px';
  star.style.animationDelay = (Math.random()*3) + 's';
  starsContainer.appendChild(star);
}

const startBtn = document.getElementById('startBtn');
const reactBtn = document.getElementById('reactBtn');
const result = document.getElementById('result');
const next = document.getElementById('nextLink');
let startTime;

startBtn.onclick = () => {
  result.textContent = 'Wait...';
  startBtn.disabled = true;
  reactBtn.disabled = true;
  reactBtn.style.backgroundColor = '';
  const delay = Math.random() * 2000 + 1500;
  setTimeout(() => {
    result.textContent = 'SABER GO!';
    reactBtn.disabled = false;
    reactBtn.style.backgroundColor = '#4CAF50';
    startTime = Date.now();
  }, delay);
};

reactBtn.onclick = () => {
  const t = Date.now() - startTime;
  result.textContent = `Reaction: ${t} ms`;
  reactBtn.style.backgroundColor = '';
  if (t < 300) {
    next.style.display = 'inline-block';
  } else {
    result.textContent += ' — Try again!';
  }
  reactBtn.disabled = true;
  startBtn.disabled = false;
};
