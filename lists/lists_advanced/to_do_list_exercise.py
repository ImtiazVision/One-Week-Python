header = """
  ____         _           
|_   _|__   __| | ___  ___ 
  | |/ _ \ / _` |/ _ \/ __|
  | (_) | (_| | (_) \__ \\
  |_|\___/ \__,_|\___/|___/
                            
"""
print(header)


while True:
  print('***********************************')
  print("Enter a command. Type 'h' for help:")
  command = input('> ')
  if command == 'q':
    break
  # Print todos from the list 