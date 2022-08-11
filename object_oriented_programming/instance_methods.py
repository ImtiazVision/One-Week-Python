# We can add a method to a class. Lets see that in action.

class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
# this add_trick() method appends a new trick to a Puppy instance's tricks list:
  def add_trick(self, new_trick):
    self.tricks.append(new_trick)
    
# nums = [1,2,3]
# nums.reverse()
# here, reverse() is a function but since it lives on an object i.e. 'nums', it is referred to as a method. 