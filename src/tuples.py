# Tuples = IMMUTABLE, ordered, sequence of arbitrary items
simple = (42, 15, 69)
differentTypes = ('Meaning', 42, True, -0.3)
newTuple = tuple('aeiou') # this creates ('a','e','i','o','u')
emptyTuple= ()

print("First: " , differentTypes[0])
print("Last: " , differentTypes[-1])

# This is a way to add an elemtn
differentTypes+= (34,56)
# error:
# otherValues[0] = 'Satan'

# of course is iterable
for v in differentTypes:
	print("Tuple: " , v)
