
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"
print(len(word))

# Write a for loop that prints out each character in the above "word" variable

for char in word:
  print(char)


# Write a while loop that does the same thing!
index = 0 # set up a variable and initiate it to 0
while index < len(word):  # if index is less than length of variable "word" (34), continue running the loop. 
  print(word[index]) 
  index += 1
  

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
number = 100

while number <= 140:
  print(number)
  number += 2



# Write a for loop that does the same thing (with range())
for number in range(100,141,2):
  print(f'for loop {number}')

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
