address = '     125 MAIN STREET     '
stripped_address = address.strip()
print(stripped_address)
formatted_address = stripped_address.lower()
print(formatted_address)

# alternatively, we can chain the methods 

email = 'RAAAZ@gmail.com   '
formatted_email = email.strip().lower()
print(formatted_email)

contact_num = '    111 444 8888    '
formatted_contact_num = contact_num.strip().replace(' ', '-')
print(formatted_contact_num)