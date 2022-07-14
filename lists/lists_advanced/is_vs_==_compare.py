# We use '==' to compare the contents inside of 2 lists. Do they hold the same values?

print([1,3] == [1,3]) # True
print([1,3] == [1,3,9]) # False
print([1,3] == [3,1]) # False

# We use 'is' to compare the identity of 2 lists. Are they the same 'container' in memory?

print([3,2,1] is [3,2,1]) # False
odd = [1,3,5]
odd1 = odd # both odd1 and odd are referring to the same list in memory container 
print(odd is odd1) # True 
print(id(odd), id(odd1))