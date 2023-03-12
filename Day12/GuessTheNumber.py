import random
logo = """
   _______ __   __ _______ _______ _______   _______ __   __ _______   __    _ __   __ __   __ _______ _______ ______   
  |       |  | |  |       |       |       | |       |  | |  |       | |  |  | |  | |  |  |_|  |  _    |       |    _ |  
  |    ___|  | |  |    ___|  _____|  _____| |_     _|  |_|  |    ___| |   |_| |  | |  |       | |_|   |    ___|   | ||  
  |   | __|  |_|  |   |___| |_____| |_____    |   | |       |   |___  |       |  |_|  |       |       |   |___|   |_||_ 
  |   ||  |       |    ___|_____  |_____  |   |   | |       |    ___| |  _    |       |       |  _   ||    ___|    __  |
  |   |_| |       |   |___ _____| |_____| |   |   | |   _   |   |___  | | |   |       | ||_|| | |_|   |   |___|   |  | |
  |_______|_______|_______|_______|_______|   |___| |__| |__|_______| |_|  |__|_______|_|   |_|_______|_______|___|  |_|
"""

print(f"Welcome to the game\n{logo}")
print("I'm thinking of a number between 1 and 100. Can you guess which one ?")
computer_number = random.choice(range(0,101))
print(f"Number is {computer_number}")
lives = 0 
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
def level(difficulty):
    if difficulty == "easy":
        return lives + 10
    elif difficulty == "hard":
        return lives + 5
    
lives = level(difficulty)
def game(lives, computer_number):
    while lives > 0:
        print(f"You have {lives} attempts")
        guess = input("Guess a number\n")
        if int(guess) > computer_number:
            print("Too high.")
            lives -= 1
        elif int(guess) < computer_number:
            print("Too low.")
            lives -= 1
        elif int(guess) == computer_number:
            print("You guessed the number. Well done .")
    else:
        print("0 Attempts left, game over.")
game(lives, computer_number)