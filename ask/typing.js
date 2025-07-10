
// typing.js

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

const promptText = document.getElementById('promptText');
const inputField = document.getElementById('inputField');
const timerEl = document.getElementById('timer');
const result = document.getElementById('result');
const nextLink = document.getElementById('nextLink');

const sentences = [
    "By the stars and Force alike, I pledge eternal loyalty to Darcy- guiding light, fierce power, unmatched greatness in all galaxies."

];

let timeLeft = 30;
let timerInterval;

function startTimer() {
  timerEl.textContent = `Time left: ${timeLeft} seconds`;
  timerInterval = setInterval(() => {
    timeLeft--;
    timerEl.textContent = `Time left: ${timeLeft} seconds`;
    if(timeLeft <= 0){
      clearInterval(timerInterval);
      finish(false);
    }
  }, 1000);
}

function finish(success) {
  inputField.disabled = true;
  if(success) {
    result.textContent = "Success! Jedi approved.";
    nextLink.style.display = "inline-block";
  } else {
    result.textContent = "Time's up! Try again.";
  }
}

function loadNewSentence() {
  const sentence = sentences[Math.floor(Math.random() * sentences.length)];
  promptText.textContent = sentence;
  inputField.value = "";
  inputField.disabled = false;
  timeLeft = 30;
  startTimer();
}

inputField.addEventListener('keydown', e => {
  if(e.key === "Enter"){
    const userInput = inputField.value.toUpperCase().trim();
    if(userInput === promptText.textContent){
      clearInterval(timerInterval);
      finish(true);
    } else {
      result.textContent = "Incorrect, keep trying!";
    }
  }
});

loadNewSentence();
