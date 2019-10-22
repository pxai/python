def hello():
	print("hello")

def add(a,b):
	return a + b

def isEven(a):
	return (a % 2 == 0)

def withDefaultValues(a, b = 0, c = 42):
	result = a + b - c
	print("Parameter values: ")
	print("a is " , a)
	print("b is " , b)
	print("c is " , c)
	return result

# calling functions
hello
hello()
a = add(600,66)
b = 0
print("Result of addition: " , add(a,b))
b = isEven(a)
print("Result of isEven for " , a , ": " , b)

withDefaultValues(5)
withDefaultValues(15,-5)
