# we can use the 'break' keyword to prematurely exit a loop. Usually this is done inside of a conditional. 
# for loop break implementation
from email import message


for char in 'cricketmatch':
  if char == 'm':
    break
  print(char)
print("End of loop")

# while loop break implementation

message = input("Please greet with a 'hi': ")

while True: # infinitely run the loop bc condition will always be True by default
  if message == 'hi': # until if the message is 'hi' break away/exit the loop
    break
  message = input("Say hi: ")
print("FINALLY! THANKS FOR SAYING HI")
  

# The 'continue' keyword end the current iteration of the loop, but does not break out of the loop.