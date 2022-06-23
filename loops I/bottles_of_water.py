
for num_bottles in range(99,0,-1):
  print(f'{num_bottles} bottles of water on the wall.')
  print(f'{num_bottles} bottles of water.')
  if num_bottles == 1:
    print(f"Take one down, pass it around, no more bottle of water on the wall.")
  else:
    print(f'Take one down, pass it around, {num_bottles - 1} bottles of water on the wall.')
  print("*" * 50)
print("*******************************") 

bottle = 99
while bottle > 0:
  print(f'{bottle} bottles of water left on the wall')
  bottle -= 1
