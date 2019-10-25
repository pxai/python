def sayHello(name=""):
	return "Hello " , name

# importing an external 'hello.py' source
# from thisfile import funcname

# If they are in different places, you need to add an emptyList
# file called __init__.py in each directory
# code/__init__.py
# code/hello.y
# other/__init__.py
# other/importSample.py
# Inside import sample:
# from code.hello import sayHello
