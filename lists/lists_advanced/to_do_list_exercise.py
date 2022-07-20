header = """
  ____         _           
|_   _|__   __| | ___  ___ 
  | |/ _ \ / _` |/ _ \/ __|
  | (_) | (_| | (_) \__ \\
  |_|\___/ \__,_|\___/|___/
                            
"""
print(header)

todos = []
completed = []
while True:
  for i in range(len(todos)):
    print(f' {i+1}) {todos[i]}')
  print('***********************************')
  print("Enter a command. Type 'h' for help:")
  command = input('> ')
  if command == 'q':
    break
  elif command == 'h':
    
  elif command.isnumeric():
    index = int(command) - 1
    if index >= len(todos):
      print("There is no todo with this number!!!")
    else:
      done_todo = todos.pop(index)
      completed.append(done_todo)
  else:
    todos.append(command)
  # Print todos from the list 
if completed:
  print(f"You have completed {len(completed)} todos today: ")
  for todo in completed:
    print(f"* {todo}")