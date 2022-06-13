# str.strip() removes the leading and trailing whitespace from a string.

msg = "  Hello World   " # removes only the leading and trailing whitespace from a string not the spaces from the middle of a string
strip = msg.strip()
print(strip)

msg1 = '--------------Hello      World----------'
strip1 = msg1.strip('-') # removes the '-' from the string 
print(strip1)