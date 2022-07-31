# Intersection (left & right): returns new set with numbers common to left and right
web_dev = {'SQL', 'css', 'html', 'JavaScript', 'Python'}
# print(web_dev)

data = {'R', 'SQL', 'Python'}
# print(data)

# Intersection of web_dev & data
print(web_dev & data)  # Output : {'Python', 'SQL'}

# Union (left | right): returns new set with members from left and right. Union is represented by a pipe (|) character.
print(web_dev | data)
# Output : {'JavaScript', 'Python', 'R', 'css', 'html', 'SQL'}
# print(web_dev.union(data))

# Difference (left - right): returns new set with members from left 'not' in right (anything from left set that is not present in right set). Here order matters and whatever set is on the left will be subtracted from the right. 

print(web_dev - data)  # output : {'css', 'html', 'JavaScript'}
print(data - web_dev)  # output : {'R'}

# Purpose of using sets:

  # - Sets make it very easy/fast to check if a value exists in a collection
  # - Sets are an easy way to remove duplicates from a collection
