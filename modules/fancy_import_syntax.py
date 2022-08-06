# Use the 'as' keyword to import a module and give it a custom name in our script. 

import random as rand
print(rand.randint(1,99))

# from...import : Use the 'from <module> import <method>' syntax to import specific pieces of a module. This is more specific and cater to specific need. We don't have to download the entire module but download specific method like 'randint' 

from random import randint
print(randint(99,110))

from math import pi, sin, cos, tan 
print(pi, sin(90), cos, tan)

# import * : We can import 'all' pieces of a given module individually using 'import *' (means import all) however this usually not the best approach to importing!

from random import *
print(randrange(1,5))