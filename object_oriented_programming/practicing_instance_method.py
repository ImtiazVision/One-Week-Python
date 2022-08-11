class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
  def add_trick(self, new_trick):
    self.tricks.append(new_trick)