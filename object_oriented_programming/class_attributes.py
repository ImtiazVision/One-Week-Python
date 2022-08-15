class Puppy:
  
  species = 'canine' # 'species' is defined on the class itself. All instances of Puppy will have the same value for 'species'. class attributes are shared across all the instances of a parent class. 
  
  def __init__(self, name):
    self.name = name
    self.tricks = []