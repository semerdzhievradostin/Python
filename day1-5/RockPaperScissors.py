import random
import sys
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
player = int(input("Let's play Rock Paper Scissors...\n Type 0 for Rock, 1 for Paper, 2 for Scissors...\n "))
if player >=3 or player < 0:
    print("Number is not valid")
    sys.exit()
print("You chose:")
print(game_images[player])
computer =  random.randint(0, 2)
print("Computer Chose:")
print(game_images[computer])
if player == 0 and computer == 2:
    print("You Win!")
elif player > computer:
    print("You Win!")
elif player == computer:
    print("It's a Draw!")
elif computer == 0 and player == 2:
    print("You Lose!")
elif computer > player:
    print("You Lose!")
