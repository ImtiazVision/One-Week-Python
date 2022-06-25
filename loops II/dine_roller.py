from random import randint

num_dice = int(input("How many dice are we rolling? "))
num_sides = int(input("How many sides on each die? "))
# 

while True:
  reply = input("Roll again? ('q' to quit)")
  if reply == 'q':
    break
  print(randint(1, num_sides))

