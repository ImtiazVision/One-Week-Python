# The 'or' operator will evaluate to True if one or both of the left or right sides evaluate to True.

day = input("Please enter what day of the week it is : ")

if day == 'saturday' or day == 'sunday':
    print("It's the weekend!")
else:
    print("It's a weekday!")