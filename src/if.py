godExists = True
if godExists:
	print("God is real unless declared integer")

## single line if
if True:print('I am single lined if')

anything = '1'
if anything:
	print("Yeah, anything different to 0 means True")

# 0, None, "", '', empty structures (),[],{} are the same as False
numberZero = 0
if not numberZero:
	print("And 0 is False")

a = b = c = 0
# we can omit or put parenthesis
if (a < b or b == c):
	print("a less than b or b equals c")


# if-else
if a > b:
	print("a is bigger than b")
else:
	print("a is NOT bigger than b")

# elif
if a > b:
	print("a is bigger than b")
elif a < b:
	print("a is less than b")
elif a == b:
	print("a and b are equal")
elif a == 0:
	pass  # this a way to do NOTHING , as we can't leave a block empty
else:
	print("a and b are alien")
