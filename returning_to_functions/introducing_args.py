# We can use the 'wildcard' or asterisk (*) notation to write functions that accept any number of arguments.

# an example of '*args' is the min() and max() function as they take 2-infinite number of arguments

print(min(1,3,5,9,2,4,6,7,8,10,-111,-94)) # output : -111 
print(max(1, 3, 5, 9, 2, 4, 6, 7, 8, 10, -111, -94)) # output: 10

# we use '*args' wildcard in front of a parameter to have infinite number of arguments when we don't know how many arguments we are providing at the time of writing a function.

# Name of the parameter (*args) can be anything we want followed by an asterisk(*) but 'args' is common but not required.


def average(*nums): # gather all remaining arguments into a tuple
  total = 0
  for arg in nums:
    total += arg # total = total + arg
  print (total/len(nums))
  return total/len(nums)

average(1,3,5)
  
