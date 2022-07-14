# split() is a string method that split a string on a given character. It returns a list that holds the split strings. 

appointment_date = '07/24/2022'

print(appointment_date.split('/'))  # ['07', '24', '2022']  here, '/' is an argument/delimiter and split() method separate the string based on '/'. Whenever, it finds '/', it split the string and returns them in a list. 

# join() is a string method that joins together the elements of an iterable/string/list into a single string. Whatever string we call it on will be used as a separator. 

team_members = ['John', 'Sal', 'Roger', 'Badman']


print(' '.join(team_members))
print('|'.join(team_members))