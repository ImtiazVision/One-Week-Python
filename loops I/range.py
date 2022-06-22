# range returns an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. Step specifies the increment/decrement. 
# Example: range(i, j) produces i, i+1, i+2, i+3, ..., j-1. Start defaults to 0, and stop is omitted. range(4) produces 0, 1, 2, 3. 
for i in range(10):
  print(i)
print("**************************")

for num in range (0,10,2):
  print(num)
print("********************************************************")

# reverse iteration
for num in range(10,1,-1):
  print(num)
print("************** Reverse Iteration *********************")
  
for i in range(0,22,2):
  print(i)
print("********************************************************")

# initializing a variable named count
count = 20
while count > 0:
  print(count)
  count -=1
