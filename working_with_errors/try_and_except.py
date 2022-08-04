# try/except: We can use try and except keywords to handle exceptions. If an exception is raised in the try block, the except block will run.


# try:
#   <code that could generate error>
# except:
#   <code that runs if error raised>

try:
  num = int(input('Please enter a number: '))
except ValueError:
  print('Oh no, that is not a number!')
