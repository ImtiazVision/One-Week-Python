# def is_even(num):
#   if num % 2 == 0:
#     return True
#   else:
#     return False
  
# result = is_even(7)
# print(result)

# def is_even(num):
#   if num % 2 == 0:
#     return True
#   return False


# result = is_even(8)
# print(result)

# best modified short function
# def is_even(num):
#   return num % 2 == 0

# result = is_even(9)
# print(result)

def slugify(phrase):
  # Here, we convert the phrase to lowercase, then remove the preceding and trailing spaces, and finally replace the empty spaces with a dash '-'.
  return phrase.lower().strip().replace(' ', '-')
  
  
phrase = slugify("   Hello there  WE ARE    HUMAN   ")
print(phrase)
