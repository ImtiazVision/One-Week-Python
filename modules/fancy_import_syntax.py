# Use the 'as' keyword to import a module and give it a custom name in our script. 

import random as rand
print(rand.randint(1,99))

# from...import : Use the 'from <module> import <method>' syntax to import specific pieces of a module 

from random import randint
print(randint(99,110))