# 'global' keyword is put in front of a variable so that it is considered as a global variable and accessible as such

def outer():
  global movie # now we are saying, 'movie' is a global variable that is available outside of this function as it has global scope
  movie = 'Spider man'
outer()

print(movie)

score = 289 

def final_score():
  global score
  score *= 2
  print(score)
final_score()
