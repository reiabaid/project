// confirmation.js

const yesBtn = document.getElementById('yesBtn');
const noBtn = document.getElementById('noBtn');
const questionContainer = document.getElementById('questionContainer');

let noClickCount = 0;
const noPhrases = [
  "Please? meow",
  "You're breaking my heart",
  "pwetty pleaseeee :/ "
];

noBtn.addEventListener('click', () => {
  if (noClickCount < noPhrases.length) {
    noBtn.textContent = noPhrases[noClickCount];
    noClickCount++;
    yesBtn.style.transform = `scale(${1 + 0.3 * noClickCount})`;
  } else {
    yesBtn.style.fontSize = "5vw";
    yesBtn.style.padding = "60px 120px";
    yesBtn.textContent = "YES ";
    noBtn.style.display = "none";
  }
});

yesBtn.addEventListener('click', () => {
  window.location.href = "yay.html";
});
