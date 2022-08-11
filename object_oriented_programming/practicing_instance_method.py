class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
  def add_trick(self, new_trick):
    self.tricks.append(new_trick)
    
  def perform_trick(self, trick): # adding another instance method 
    if trick in self.tricks:
      print(f"{self.name} performs {trick}")
    else:
      print(f"{self.name} does not know {trick}")