# We can raise our own exceptions (force them to happen) whenever we want, using the 'raise' keyword.We can also provide a specific message when raising an exception. raise ValueError('invalid character')
# print('Hello World')

# 'hello'[6]


# print("Goodbye")

from curses.ascii import isalpha


def get_user_name():
  input1 = input('please enter your name: ')
  print(input1)
  if not input1.isalpha():
    raise ValueError('please enter alpha characters only')
  return input1

def register_user():
  user = get_user_name()
  Database.save(user)