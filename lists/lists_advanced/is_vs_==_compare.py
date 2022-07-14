# We use '==' to compare the contents inside of 2 lists. 

print([1,3] == [1,3]) # True
print([1,3] == [1,3,9]) # False
print([1,3] == [3,1]) # False

# We use 'is' to compare the identity of 2 lists. 

print([3,2,1] is [3,2,1]) # False