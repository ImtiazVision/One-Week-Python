# To define a class, first thing we need is the 'class' keyword and class name is Capitalized.

# __init__ is a special method that is automatically called whenever a new class i.e. Puppy is created(instantiated). 
class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []