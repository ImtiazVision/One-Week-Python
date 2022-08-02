# def add_twice(value, list1=[]):
#   list1.append(value)
#   list1.append(value)
#   print(list1)

def add_twice(value, list1=None):
  if list1 is None:
    list1 = []
  list1.append(value)
  list1.append(value)
  print(list1)

add_twice('1',[1,2,3])
add_twice('1',[])