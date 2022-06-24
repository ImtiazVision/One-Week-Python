# nested loops are loops inside a loop

for outer in range(1,6):
  print(outer)
  for inner in range(1,11):
    print("\t", inner)