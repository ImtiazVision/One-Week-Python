# To access elements of a tuple, we use index of that element 
dishes = ('burrito', 'taco', 'quesadilla', 'fajita')
print(dishes[2])
# we can also use .index() method to ask for index of an element by providing its name inside the index method
print(dishes.index('fajita'))

# Slicing of tuple
print(dishes[0:3]) # 0,1,2 but 3rd element is omitted