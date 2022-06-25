from random import randint

num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))
# 

while True:
  input("Roll again? ('q' to quit)")
  print(randint(1, num_sides))

