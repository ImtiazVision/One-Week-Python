address = '     125 MAIN STREET     '
stripped_address = address.strip()
print(stripped_address)
formatted_address = stripped_address.lower()
print(formatted_address)

# alternatively, we can chain the methods 

email = 'RAAAZ@gmail.com   '
formatted_email = email.strip().lower()
print(formatted_email)