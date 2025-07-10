// index.js
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
const moon = document.querySelector('.moon');
moon.style.top = Math.random()*100 + 'vh';