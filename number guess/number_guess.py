import random
secret_number= random.randint(1, 100)
attempts = 0
max_attempts = 3
while True:
    guess = input("Guess the number (between 1 and 100): ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    attempts += 1
    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break


     # Add hint after 5 incorrect attempts
    if attempts == 5:
        # Choose one hint to show
        if secret_number % 2 == 0:
            print("🔎 Hint: The number is even.")
        else:
            print("🔎 Hint: The number is odd.")