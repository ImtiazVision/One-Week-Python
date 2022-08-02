# Argument Unpacking: turning sequences into separate args. 

def average(*args):
  print(args)
  total = 0
  for arg in args:
    total += arg
  print(total/len(args))
  
nums = [8,2,1,3,9,6,7]

#average(nums)  # TypeError
# Instead, we can 'unpack' the list into individual args using an asterisks. 

average(*nums)
