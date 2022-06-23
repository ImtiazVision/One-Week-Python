from pyrsistent import b


for num in range(100,0,-1):
  print(f'{num} bottles of water left on the wall')
print("*******************************") 

bottle = 99
while bottle > 0:
  print(f'{bottle} bottles of water left on the wall')
  bottle -= 1
