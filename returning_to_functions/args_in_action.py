def count_stuff(*args):
  print(f"You have passed me {len(args)} arguments")
  
count_stuff(1,2,3,4,5)


def add(*nums):
  total = 0
  for num in nums:
    total += num
  print(total)

add(2,3,5)

def exception (first, second, *others):
  print(f"first is {first}")
  print(f"second is {second}")
  print(f"others are{others}")
  
exception(True, 'string', 2,3,5)
