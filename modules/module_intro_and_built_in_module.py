# Module: A module is simply a Python file that contains code that can be re-used in other files.

# Modules allow us to break up complex programs into smaller, more manageable pieces across multiple files. 

# There are 3 types of modules: 1. Built-in 2. Custom 3. 3rd Party

# Built-in Module: Standard Library
# Python comes with tons of built-in modules that we can use, if we import them. Each module consists of methods and functionality bundled together. 

# To use a module, we must import it first using the import keyword.

# import random
# print(random.randint(1,5))
# from random import randint
# print(randint(1,8))

# importing calender module
import calendar
print(calendar.isleap(2024))
print(calendar.weekday(2010,4,22))
