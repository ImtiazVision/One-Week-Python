# list[start:stop:step]

wish_list = ['house', 'car', 'money', 'peace', 'fame', 'Airplane', 'Yacht', 'Palace', 'Rolex', 'Mercedes']

print(wish_list[1:4])  # ['car', 'money', 'peace']
print(wish_list[0:9:2])  # ['house', 'money', 'fame', 'Yacht', 'Rolex']
print(wish_list[0:])  # ['house', 'car', 'money', 'peace', 'fame', 'Airplane', 'Yacht', 'Palace', 'Rolex', 'Mercedes']
print(wish_list[:])  # ['house', 'car', 'money', 'peace', 'fame', 'Airplane', 'Yacht', 'Palace', 'Rolex', 'Mercedes']
print(wish_list[::2])  # ['house', 'money', 'fame', 'Yacht', 'Rolex']
# we can not only replace specific elements but also add new sequence of lists into the old one
wish_list[2:6] = [1, 2, 3, 4, 5]
print(wish_list[:])  # ['house', 'car', 1, 2, 3, 4, 5, 'Yacht', 'Palace', 'Rolex', 'Mercedes']
