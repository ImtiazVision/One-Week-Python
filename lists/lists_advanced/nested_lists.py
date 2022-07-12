# nested lists are lists inside a list

from xml.sax.saxutils import prepare_input_source


list1 = [1, 'hi', True, [], ['hello', False, 4.99]]

multi_dimensional_list = [[[[[]]]]] # total 5 lists nested 

# accessing stuff from a nested list is done by adding [][] subsequently depending on how many nested lists exist

nums = [1,2,3,4, [5,6]]
print(nums[4]) # [5,6]

print(nums[4][0]) # [5]

team = [
  ['John', "Walker"],
  ['Will', 'Smith'],
  ["Sam", "Ronald"]
]

print(team[1][1])

for members in team:
  # print(members)
  for player in members:
    print(player)