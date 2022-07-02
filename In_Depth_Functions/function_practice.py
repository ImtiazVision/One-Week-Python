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

# def slugify(phrase):
  # Here, we convert the phrase to lowercase, then remove the preceding and trailing spaces, and finally replace the empty spaces with a dash '-'.
  # return phrase.lower().strip().replace(' ', '-')
    
# phrase = slugify("   Hello there  WE ARE    HUMAN   ")
# print(phrase)

def vowel_counter(word):
  # we  need a counter to count how many times we encounter a vowel while looping over every character of argument 'word', so we add one and set it equal to 0
  
  count = 0
  for each_character in word:
    # to check if the character is a vowel, we can use the 'in' keyword
    if each_character in 'aeiou':
      count += 1
    return count
total_number_of_vowels = vowel_counter('apple') # since the function is returning the count of vowels, we need to store function call with arguments in a variable and then print it on the console. 
    