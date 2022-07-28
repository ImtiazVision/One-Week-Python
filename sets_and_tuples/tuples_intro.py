# Tuples are similar to a weak list. They are ordered collections of diverse items, but they are immutable, which means that we can't modify the contents inside a tuple once it exists, after it's been constructed. In that they are sorted indexed collections, they are similar to lists. Every element has a unique index, but they differ in that we cannot modify them after they have been created. This also implies that we have significantly fewer methods. We can't perform things like append, sort, or remove, or pop since they all change the structure of a list but it doesn't apply to tuples since they are immutable. 

# Create a Tuple
# To define a tuple, we use parenthesis on each side, followed by commas to split our values within.

dishes = ('burrito', 'taco', 'quesadilla', 'fajita')

# Empty Tuple

empty_tuple = ()
empty_tuple = tuple()

