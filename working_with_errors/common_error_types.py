# Common errors are:
# KeyError, ValueError, SyntaxError, NameError, IndexError, TypeError

# SyntaxError
# print(@)  # SyntaxError: invalid syntax
# print(while a > 9)  # SyntaxError: invalid syntax

# NameError 
# NameError occurs when we try to access a variable that doesn't exists. 
# print(asdf)  # NameError: name 'asdf' is not defined

# IndexError
# IndexError occurs when we try to access an index that doesn't exists be it a string ' ' or tuple ()

# print('hello'[5])  # IndexError: string index out of range

# print((1, 2, 3)[3])  # IndexError: tuple index out of range

# TypeError
# TypeError occurs when we try to do any operations that are not allowed or incompatible between 2 different data types. For example, if we try to add an int to a string.

# print(1 + 'one')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ValueError
# ValueError raised when an operation or function receives an argument that has the right type but an inappropriate value. 

# print(int('1')) # this works 
# print(int('a'))  # ValueError: invalid literal for int() with base 10: 'a'


# KeyError
# KeyError occurs when we try to access a key in a dictionary that is not there. 

dictionary = {'first_key': 11}
print(dictionary['first_key']) # this works because the key exists
print(dictionary['one'])  # KeyError: 'one'
