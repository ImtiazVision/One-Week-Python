# list1 = [1,2,3,4,5,6,7,8,9,10]

# total = 0

# for element in list1:
#   total = total + element

# average = total/ len(list1)
# print(total, average)

def average(numbers):
  total = 0
  for num in numbers:
    total += num
  print(total/len(numbers))
  return total/len(numbers)
  


average([2,4,6,8])