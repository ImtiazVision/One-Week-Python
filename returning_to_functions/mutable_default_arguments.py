# def add_twice(value, list1=[]):
#   list1.append(value)
#   list1.append(value)
#   print(list1)

# to fix the mutable default parameter 'list1', we set it equal to 'None' and create an empty new list each time function gets called. 

def add_twice(value, list1=None):
  if list1 is None:
    list1 = []
  list1.append(value)
  list1.append(value)
  print(list1)

add_twice('1',[1,2,3])
add_twice('1',[])