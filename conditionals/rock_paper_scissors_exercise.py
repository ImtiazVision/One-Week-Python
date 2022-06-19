from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
        _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
      __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1, 3)

# Turn that random number into the computer's RPS move
if num == 1:
  computer_move = "rock"
elif num == 2:
  computer_move = "paper"
else:
  computer_move = "scissors"


# Ask a user to enter their move


# Print the rock, paper, or scissors ASCII art that corresponds to the player's move


# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move


# Figure out who wins and print the result!
