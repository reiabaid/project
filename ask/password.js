const correctPassword = "darcy is the best";

const decoyPasswords = [
  "darcy rules the galaxy",
  "darcy the jedi master",
  "darcy is the almighty"
];

// Combine correct + decoys and shuffle
const allPasswords = [correctPassword, ...decoyPasswords];

// Shuffle helper function
function shuffle(array) {
  for(let i = array.length -1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

const shuffledPasswords = shuffle(allPasswords.slice()); // create a shuffled copy

// Show options
const optionsDiv = document.getElementById('passwordOptions');
shuffledPasswords.forEach(pwd => {
  const div = document.createElement('div');
  div.textContent = pwd;
  optionsDiv.appendChild(div);
});

const input = document.getElementById('passwordInput');
const submitBtn = document.getElementById('submitBtn');
const message = document.getElementById('message');

submitBtn.addEventListener('click', () => {
  const userInput = input.value.trim();

  if (userInput === "") {
    message.style.color = '#ff5555';
    message.textContent = "Please enter a password.";
    return;
  }

  if (userInput === correctPassword) {
    message.style.color = '#00ff00';
    message.textContent = "Correct! You cracked the password! 🚀";
    setTimeout(() => {
      window.location.href = "typing.html"; // link to next page
    }, 2000);
  } else {
    message.style.color = '#ff5555';
    message.textContent = "Wrong password. Try again!";
  }
});

// Allow enter key to submit
input.addEventListener('keyup', (e) => {
  if (e.key === 'Enter') submitBtn.click();
});
