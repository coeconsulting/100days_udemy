### ROCK, PAPER, SCISSORS ###
import random

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
choice = int(input("Welcome to a game of Rock, Paper, Scissors. What do you chosse? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
computer_choice = random.randint(0,2)
print(f"Computer chose:\n{computer_choice}")

if choice == computer_choice:
    print("It's a draw")
elif computer_choice - choice == 1 or computer_choice - choice == -2:
    print("You lose")
else:
    print("You win")

### ROOKIE SOLLUTION: ###

# if choice == "0":
#     print(rock)
# elif choice == "1":
#     print(paper)
# else:
#     print(scissors)

# if choice == "0" and computer_choice == paper:
#     print("You lose")
# elif choice == "0" and computer_choice == scissors:
#     print("You win")
# elif choice == "0" and computer_choice == rock:
#     print("It's a draw")

# elif choice == "1" and computer_choice == paper:
#     print("It's a draw")
# elif choice == "1" and computer_choice == scissors:
#     print("You lose")
# elif choice == "1" and computer_choice == rock:
#     print("You win")

# elif choice == "2" and computer_choice == paper:
#     print("You win")
# elif choice == "2" and computer_choice == scissors:
#     print("It's a draw")
# elif choice == "2" and computer_choice == rock:
#     print("You lose")