# We can add a method to a class. Lets see that in action.

class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
# this add_trick() method appends a new trick to a Puppy instance's tricks list:
  def add_trick(self, new_trick):
    self.tricks.append(new_trick)