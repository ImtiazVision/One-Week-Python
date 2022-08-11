class Dog:
  def __init__(self, name, breed, location):
    self.name = name
    self.breed = breed
    self.location = location
    self.tricks = []
    
german = Dog('Elmo','German Shepard', 10001)
print(german.name)
print(german.breed)
print(german.location)

print(isinstance(german, Dog)) # isinstance will tell whether german meets the requirements of a class Dog. In this case, it's True. 