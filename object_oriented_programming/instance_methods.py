# We can add a method to a class. Lets see that in action.
# the first parameter is always self and it refers to the particular instance that has been created. 
class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
# this add_trick() method appends a new trick to a Puppy instance's tricks list:
  def add_trick(self, new_trick):
    self.tricks.append(new_trick)
# Call it on an instance: 
# Calling add_trick() on Airedale Terrier adds 'sit' to his trick
    
# nums = [1,2,3]
# reverse = nums.reverse()
# print(reverse)
# here, reverse() is a function but since it lives on an object i.e. 'nums', it is referred to as a method. 