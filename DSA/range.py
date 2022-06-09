
# The function is expected to print an INTEGER.
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#  3. INTEGER stepvalue
#

def rangefunction(startvalue, endvalue, stepvalue):
    i = startvalue
    while i < endvalue:
      yield i
      i += stepvalue
for i in range(2, 9, 2):
        print(i**2)



