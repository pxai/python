# dictionaries are like hashes
ages = {'Gandalf':1432, 'Aragorn':543, 'Bilbo':112}
emptyDictionary = {}

# using the builtin function:
trigValues = dict(sin=34, cos=353.23, tan=34)
otherAges = dict([['Frodo',34], ['Samwise',35]])

ages['Bilbo'] = 120
ages['Radagast'] = 1423

# iterating...
for key in ages:
	print key , " : " , ages[key]
