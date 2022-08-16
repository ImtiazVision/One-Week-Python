# The main idea behind inheritance is that multiple class can share functionalities between them. 
class Cat:
  def __init__(self,name):
    self.name = name
  def meow(self):
    print(f"{self.name} meows")
    
# The following Lion class inherits from the base class Cat on line 9.

class Lion(Cat):
  def roar(self):
    print(f"{self.name} roars")
    
# eli is a Lion, but it can meow because Lion inherits functionalities from base class Cat. 

eli = Lion('Eli')
eli.meow() # Eli meows