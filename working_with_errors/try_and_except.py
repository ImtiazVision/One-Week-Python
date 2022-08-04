# try/except: We can use try and except keywords to handle exceptions. If an exception is raised in the try block, the except block will run.


# try:
#   <code that could generate error>
# except:
#   <code that runs if error raised>


# example of try and except

# we use 'try' when we know an error might or might not happen.
try:
  num1 = int(input('Enter a number: '))
except:
  print('You entered something that is not a number, we have a default value for all non-number that is: 5')
  num1 = 5

print(f"You have entered {num1}")


# Usually, it's better to except a specific exception and handle it, rather than handling any possible exception that could occur. 
try:
  num = int(input('Please enter a number: '))
except ValueError: # here, we are saying only handle ValueError
  print('Oh no, that is not a number!')

# Multiple Excepts
try:
  num2 = int(input("Enter an integer: "))
  print(10/num2)
except ValueError:
  print("That's not an int!")
except ZeroDivisionError:
  print("Can't divide by zero!")
except EOFError:
  print("YOU DIDN'T ENTER ANYTHING!")