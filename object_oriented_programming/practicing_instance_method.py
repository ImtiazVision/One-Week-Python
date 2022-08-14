class Puppy:
  def __init__(self, name):
    self.name = name
    self.tricks = []
    
  def add_trick(self, new_trick):
    self.tricks.append(new_trick)
    
  def perform_trick(self, trick): # adding another instance method perform_trick and it will perform a trick if a Puppy instance knows the trick.
    if trick in self.tricks:
      print(f"{self.name} performs {trick}")
    else:
      print(f"{self.name} does not know {trick}")
# Each Puppy instance is a different object and has unique actions if we want to provide so. Affenpinscher knows 'sit' but doesn't know 'stay'. 

# Affenpinscher
affenpinscher = Puppy("Affenpinscher")
affenpinscher.add_trick('sit')

affenpinscher.perform_trick('sit')

affenpinscher.perform_trick('stay')

# Akita
akita = Puppy('Akita')
akita.add_trick('sit')
akita.add_trick('down')
akita.add_trick('stay')

akita.perform_trick('stay')