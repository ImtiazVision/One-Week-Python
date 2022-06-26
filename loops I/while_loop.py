# while loop repeats a block of code as long as the condition is true. While loop is very similar to if statement except that is repeats the code block until the condition is false.
# while condition:
#     code block

# For example,
# if x < 10:
    # print('something')
# In this case python only checks the above condition once and if it is true it will print the statement.
# Whereas if we replace "if" with "while" it will repeat the code block until the condition is false.

# x = 9

# while x > 0:
#   print(x)
#   x -= 1 

# count = 0
# while count <= 5:
#     print(count)
#     count += 1

# num = 15

# while num > 0:
#     print(f"Number is {num}")
#     num -= 1
    

# num = 0

# while num < 10 :
  # print(f"Number is {num}")
  # num += 1 # increment the number from 0 to all the way to 9
# print("After the loop")


count = 0

while count < 8:
  print("*" * count)
  count +=1
  
count = 8

while count > 0:
  print("*" * count)
  count -=1
  
  
count = 1
while count <= 10:
  print('loop in progress')
  count += 1