class Dog:
  def __init__(self, name, breed, location):
    self.name = name
    self.breed = breed
    self.location = location
    self.tricks = []
  def bark(self):
    print(f"{self.name} says WOOF!")
  def learn_trick(self, new_trick):
    if new_trick not in self.tricks:
      self.tricks.append(new_trick)
    
german = Dog('Elmo','German Shepard', 10001)
print(german.name)
print(german.breed)
print(german.location)
print(german.bark())

print(isinstance(german, Dog)) # isinstance will tell whether german meets the requirements of a class Dog. In this case, it's True. 
# isinstance? return whether an object is an instance of a class or of a subclass thereof.

max = Dog('Max','American Eskimo', 99932)
print(max.name)
print(max.breed)
print(max.location)

# class is a blueprint 
