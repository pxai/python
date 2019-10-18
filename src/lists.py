# Lists, array-like mutable
langs = ['Python','Ruby','JavaScript']
otherList = ['God',666, True]
emptyList = []

print("First: " , langs[0])
print("Last: " , langs[-1])

# This is a way to add an elemtn
langs += ['NodeJS']
otherList[0] = 'Satan'

for x in langs:
	print("Languages : " , x)
