# import random
# print(random.randint(1,6))
# print(random.randint(1,6))
# print(randint(1,6))
# print(randint(2,11))
# print(randint(3,9))

from random import randint
toss = randint(0,1)
if toss == 0:
  print("Heads")
else:
  print("Tails")

